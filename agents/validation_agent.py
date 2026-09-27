from graph.state import SupplyChainState


def validation_agent(state: SupplyChainState) -> dict:
    analysis = state.get("analysis_result", {})
    feedback: list[str] = []

    if not analysis:
        feedback.append("Analysis result is missing.")

    if not analysis.get("recommendations"):
        feedback.append("At least one recommendation is required.")

    revision_count = state.get("revision_count", 0)

    if feedback:
        return {
            "validation_status": "needs_revision",
            "validation_feedback": feedback,
            "revision_count": revision_count + 1,
            "execution_log": ["Validation requested a revision"],
        }

    return {
        "validation_status": "approved",
        "validation_feedback": [],
        "final_response": analysis,
        "execution_log": ["Analysis approved"],
    }