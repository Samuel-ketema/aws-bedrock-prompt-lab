def summarize_prompt(text):

    return f"""
Human: Summarize the following text in 3 sentences.

{text}

Assistant:
"""


def classify_prompt(text):

    return f"""
Human: Classify the sentiment of this text as Positive, Negative, or Neutral.

{text}

Assistant:
"""


def extract_prompt(text):

    return f"""
Human: Extract name, company, and email from this text and return JSON.

{text}

Assistant:
"""
