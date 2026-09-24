from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from app.agents.retrieval_agent import retrieve
from app.services.llm import generate_answer

class AgentState(TypedDict, total=False):
    question: str
    route: str
    contexts: list[dict]
    answer: str
    grounded: bool

def classify(state: AgentState):
    question = state["question"].lower()
    route = "knowledge_retrieval"
    if any(word in question for word in ["hello", "hi", "hey"]):
        route = "greeting"
    return {"route": route}

def retrieval(state: AgentState):
    return {"contexts": retrieve(state["question"])}

def respond(state: AgentState):
    if state["route"] == "greeting":
        return {"answer": "Hello. I can help answer questions from the enterprise knowledge base.", "grounded": True}
    answer = generate_answer(state["question"], state.get("contexts", []))
    grounded = bool(state.get("contexts"))
    return {"answer": answer, "grounded": grounded}

builder = StateGraph(AgentState)
builder.add_node("classify", classify)
builder.add_node("retrieval", retrieval)
builder.add_node("respond", respond)
builder.add_edge(START, "classify")
builder.add_edge("classify", "retrieval")
builder.add_edge("retrieval", "respond")
builder.add_edge("respond", END)
graph = builder.compile()

def run_agent(question: str):
    result = graph.invoke({"question": question})
    sources = [
        {"document": c["document"], "score": round(c["score"], 4)}
        for c in result.get("contexts", [])
    ]
    return {
        "answer": result["answer"],
        "sources": sources,
        "route": result["route"],
        "grounded": result["grounded"],
    }
