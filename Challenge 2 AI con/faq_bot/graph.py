# 🔄 LangGraph setup

from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from .schema import FAQState
from .logic import get_best_faq_answer

def build_graph():
    answer_node = RunnableLambda(get_best_faq_answer)

    graph_builder = StateGraph(FAQState)
    graph_builder.add_node("get_answer", answer_node)
    graph_builder.set_entry_point("get_answer")
    graph_builder.set_finish_point("get_answer")

    return graph_builder.compile()
