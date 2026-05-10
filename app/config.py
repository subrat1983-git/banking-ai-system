import os
from dotenv import load_dotenv

load_dotenv()




class Settings :
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DB_URL = os.getenv("DB_URL","sqlite:///./tickets.db")


settings = Settings()