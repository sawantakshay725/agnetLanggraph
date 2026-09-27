from langgraph.graph import StateGraph

from agents.analysis_agent import analysis_agent
from agents.demand_agent import demand_agent
from agents.inventory_agent import inventory_agent
from agents.supplier_agent import supplier_agent
from agents.validation_agent import validation_agent
from graph.router import validation_router
from graph.state import SupplyChainState

START = "__start__"
END = "__end__"

def finish_node(state: SupplyChainState) -> dict:
    if state.get("final_response"):
        return {}

    return {
        "final_response": {
            "analysis": state.get("analysis_result", {}),
            "validation_status": state.get("validation_status"),
            "validation_feedback": state.get(
                "validation_feedback", []
            ),
            "errors": state.get("errors", []),
        }
    }


def build_supply_chain_graph():
    builder = StateGraph(SupplyChainState)

    # Nodes
    builder.add_node("demand_agent", demand_agent)
    builder.add_node("inventory_agent", inventory_agent)
    builder.add_node("supplier_agent", supplier_agent)
    builder.add_node("analysis_agent", analysis_agent)
    builder.add_node("validation_agent", validation_agent)
    builder.add_node("finish", finish_node)

    # Run domain agents in parallel
    builder.add_edge(START, "demand_agent")
    builder.add_edge(START, "inventory_agent")
    builder.add_edge(START, "supplier_agent")

    # Join agent outputs
    builder.add_edge("demand_agent", "analysis_agent")
    builder.add_edge("inventory_agent", "analysis_agent")
    builder.add_edge("supplier_agent", "analysis_agent")

    builder.add_edge("analysis_agent", "validation_agent")

    # Validation loop
    builder.add_conditional_edges(
        "validation_agent",
        validation_router,
        {
            "revise_analysis": "analysis_agent",
            "finish": "finish",
        },
    )

    builder.add_edge("finish", END)

    return builder.compile()


supply_chain_graph = build_supply_chain_graph()