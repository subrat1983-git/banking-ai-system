from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from app.database import Base

class SupportTicket(Base):
    __tablename__ = 'support_tickets'

    ticket_id = Column(Integer,primary_key=True,index=True)
    message = Column(String,nullable=False)
    status = Column(String,nullable=False,default="OPEN")
    created_at = Column(DateTime, default=datetime.now)