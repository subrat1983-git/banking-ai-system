from langgraph.graph import StateGraph, END
from langsmith import traceable

from app.graph.state import AgentState
from app.graph.memory import get_memory, save_memory

from app.agents.classifier_agent import classify_message
from app.agents.feedback_agent import (
    handle_positive_feedback,
    handle_negative_feedback
)
from app.agents.query_agent import handle_query


def classifier_node(state):

    category = classify_message(
        state["user_input"],
        state["history"]
    )

    return {
        **state,
        "category": category
    }


def feedback_node(state):

    if "Positive" in state["category"]:

        response = handle_positive_feedback()

    else:

        response = handle_negative_feedback(
            state["user_input"]
        )

    return {
        **state,
        "response": response
    }


def query_node(state):

    response = handle_query(
        state["user_input"],
        state["history"]
    )

    return {
        **state,
        "response": response
    }


def route(state):

    if "Query" in state["category"]:
        return "query"

    return "feedback"


graph_builder = StateGraph(AgentState)

graph_builder.add_node(
    "classifier",
    classifier_node
)

graph_builder.add_node(
    "feedback",
    feedback_node
)

graph_builder.add_node(
    "query",
    query_node
)

graph_builder.set_entry_point(
    "classifier"
)

graph_builder.add_conditional_edges(
    "classifier",
    route,
    {
        "feedback": "feedback",
        "query": "query"
    }
)

graph_builder.add_edge("feedback", END)
graph_builder.add_edge("query", END)

graph = graph_builder.compile()


@traceable(name="LangGraph Workflow")
def run_workflow(user_input, session_id):

    history = get_memory(session_id)

    result = graph.invoke({
        "user_input": user_input,
        "category": None,
        "response": None,
        "ticket_id": None,
        "history": history
    })

    updated_history = history + [
        f"User: {user_input}",
        f"Bot: {result['response']}"
    ]

    save_memory(
        session_id,
        updated_history
    )

    return result