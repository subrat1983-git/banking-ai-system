from typing import TypedDict,Optional,List

class AgentState(TypedDict):
    user_input : str
    category : Optional[str]
    response : Optional[str]
    ticket_id : Optional[int]
