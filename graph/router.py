from typing import Literal

from graph.state import SupplyChainState


def validation_router(
    state: SupplyChainState,
) -> Literal["revise_analysis", "finish"]:
    status = state.get("validation_status")
    revisions = state.get("revision_count", 0)
    max_revisions = state.get("max_revisions", 2)

    if status == "needs_revision" and revisions <= max_revisions:
        return "revise_analysis"

    return "finish"