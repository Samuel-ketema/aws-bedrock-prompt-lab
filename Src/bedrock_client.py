import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

def invoke_model(prompt):

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 300,
        "temperature": 0.5
    })

    response = client.invoke_model(
        modelId="anthropic.claude-v2",
        body=body
    )

    result = json.loads(response["body"].read())

    return result["completion"]
