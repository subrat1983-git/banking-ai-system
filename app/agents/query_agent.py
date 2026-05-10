import re
from langsmith import traceable
from app.services.ticket_service import get_ticket

def extract_ticket_id(text):

    match = re.search(r"\b\d{6}\b", text)

    if match:
        return int(match.group())

    return None


@traceable(name="Query Agent")
def handle_query(user_input, history=[]):

    if "last ticket" in user_input.lower():

        for item in reversed(history):

            ticket = extract_ticket_id(item)

            if ticket:
                ticket_id = ticket
                break
        else:
            return "No previous ticket found."

    else:
        ticket_id = extract_ticket_id(user_input)

    if not ticket_id:
        return "Please provide valid ticket number."

    ticket = get_ticket(ticket_id)

    if not ticket:
        return f"Ticket #{ticket_id} not found."

    return (
        f"Your ticket #{ticket_id} "
        f"is currently marked as: "
        f"{ticket.status}."
    )