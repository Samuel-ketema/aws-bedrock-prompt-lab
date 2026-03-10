from bedrock_client import invoke_model
from prompts import summarize_prompt

text = """
Artificial intelligence is transforming industries by enabling automation,
predictive analytics, and intelligent decision making.
"""

prompt = summarize_prompt(text)

response = invoke_model(prompt)

print(response)
