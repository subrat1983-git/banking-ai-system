import random
from openai import OpenAI
from langsmith import traceable

from app.config import settings
from app.services.ticket_service import create_ticket

client = OpenAI(api_key=settings.OPENAI_API_KEY)

@traceable(name="Positive Feedback Agent")
def handle_positive_feedback():

    prompt = """
    Generate a warm thank you message
    for banking customer feedback.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


@traceable(name="Negative Feedback Agent")
def handle_negative_feedback(message):

    ticket_id = random.randint(100000, 999999)

    create_ticket(ticket_id, message)

    return (
        f"We apologize for the inconvenience. "
        f"A new ticket #{ticket_id} has been generated. "
        f"Our team will follow up shortly."
    )