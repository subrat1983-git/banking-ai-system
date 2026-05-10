from fastapi.openapi.models import APIKey
from openai import OpenAI
from langsmith import traceable
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def classify_message(user_input,history=[]):

    history_text= "\n".join(history)
    prompt = f"""
       Conversation History:
       {history_text}

       Classify this banking support message into:
       - Positive Feedback
       - Negative Feedback
       - Query

       Message:
       {user_input}

       Return only category.
       """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()