from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.config import settings

engine = create_engine(settings.DB_URL,connect_args={'check_same_thread': False})
session = sessionmaker(bind=engine,autoflush=False, expire_on_commit=False)
Base = declarative_base()