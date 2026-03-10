from bedrock_client import invoke_model
from prompts import classify_prompt

text = "The product works great but customer support was slow."

prompt = classify_prompt(text)

response = invoke_model(prompt)

print(response)
