from app.database import session
from app.models.ticket import SupportTicket

def create_ticket(ticket_id,message):
    db = session()
    ticket = SupportTicket(ticket_id=ticket_id,message=message)
    db.add(ticket)
    db.commit()
    db.close()

def get_ticket(ticket_id):
    db = session()
    ticket = db.query(SupportTicket).filter(SupportTicket.ticket_id == ticket_id).first()
    db.close()
    return ticket


