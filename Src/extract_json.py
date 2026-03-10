from bedrock_client import invoke_model
from prompts import extract_prompt

text = """
John Smith works at Amazon.
His email is johnsmith@email.com
"""

prompt = extract_prompt(text)

response = invoke_model(prompt)

print(response)
