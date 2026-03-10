def summarize_prompt(text: str) -> str:
    return f"""
Human: Summarize the following text in 3 concise sentences.

{text}

Assistant:
"""


def classify_prompt(text: str) -> str:
    return f"""
Human: Classify the sentiment of this text as one of:
Positive, Negative, or Neutral.

Return only the label.

Text:
{text}

Assistant:
"""


def extract_prompt(text: str) -> str:
    return f"""
Human: Extract the following fields from the text and return valid JSON only.

Fields:
- name
- company
- email

Text:
{text}

Assistant:
"""
