from fastapi import FastAPI
from pydantic import BaseModel

from app.database import Base, engine
from app.graph.workflow import run_workflow

Base.metadata.create_all(bind=engine)

app = FastAPI()

class UserRequest(BaseModel):
    session_id: str
    message: str


@app.post("/chat")
def chat(request: UserRequest):

    result = run_workflow(
        request.message,
        request.session_id
    )

    return result