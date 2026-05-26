import json
import os
from datetime import datetime, timezone

import boto3

s3 = boto3.client("s3")
bedrock = boto3.client("bedrock-runtime")
dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ["TABLE_NAME"]
MODEL_ID = os.environ["MODEL_ID"]


def handler(event, context):
    job_id = event["jobId"]
    bucket = event["bucket"]
    transcript_key = event["transcriptKey"]
    table = dynamodb.Table(TABLE_NAME)

    try:
        transcript_obj = s3.get_object(Bucket=bucket, Key=transcript_key)
        transcript = transcript_obj["Body"].read().decode("utf-8")

        prompt = build_prompt(transcript)
        report = invoke_bedrock(prompt)

        report_key = f"reports/{job_id}/report.json"
        s3.put_object(
            Bucket=bucket,
            Key=report_key,
            Body=json.dumps(report, ensure_ascii=False, indent=2).encode("utf-8"),
            ContentType="application/json",
        )

        table.update_item(
            Key={"jobId": job_id},
            UpdateExpression="SET #s = :status, reportS3Key = :report, updatedAt = :updated",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={
                ":status": "COMPLETED",
                ":report": report_key,
                ":updated": now_iso(),
            },
        )

        return {"jobId": job_id, "status": "COMPLETED", "reportS3Key": report_key}

    except Exception as exc:
        table.update_item(
            Key={"jobId": job_id},
            UpdateExpression="SET #s = :status, errorMessage = :error, updatedAt = :updated",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={
                ":status": "FAILED",
                ":error": str(exc),
                ":updated": now_iso(),
            },
        )
        raise


def build_prompt(transcript):
    return f"""
You are a communication coach helping a student improve reasoning and explanation skills.

Analyze the transcript below. Do not answer as the student. Provide coaching feedback.

Return valid JSON with:
- summary
- mainTopic
- strongPoints
- weakReasoning
- improvedResponse with claim, reason, evidence, example
- whyQuestions
- safetyNote
- vietnameseSummary

Transcript:
{transcript}
"""


def invoke_bedrock(prompt):
    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ],
        inferenceConfig={
            "maxTokens": 1200,
            "temperature": 0.2,
        },
    )
    text = response["output"]["message"]["content"][0]["text"]

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"rawModelOutput": text}


def now_iso():
    return datetime.now(timezone.utc).isoformat()
