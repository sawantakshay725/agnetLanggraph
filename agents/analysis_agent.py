from graph.state import SupplyChainState


def analysis_agent(state: SupplyChainState) -> dict:
    revision_feedback = state.get("validation_feedback", [])

    analysis = {
        "query": state.get("query"),
        "demand": state.get("demand_result", {}),
        "inventory": state.get("inventory_result", {}),
        "supplier": state.get("supplier_result", {}),
        "recommendations": [],
        "revision_feedback": revision_feedback,
    }

    # Replace this section with your LLM or deterministic analysis.
    if state.get("inventory_result"):
        analysis["recommendations"].append(
            "Review inventory levels against forecast demand."
        )

    return {
        "analysis_result": analysis,
        "validation_status": "pending",
        "execution_log": ["Combined supply-chain analysis completed"],
    }