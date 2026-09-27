from operator import add
from typing import Annotated, Any, Literal, TypedDict


class SupplyChainState(TypedDict, total=False):
    # Input
    query: str
    product_id: str | None
    supplier_id: str | None
    location_id: str | None
    forecast_horizon: int

    # Agent outputs
    demand_result: dict[str, Any]
    inventory_result: dict[str, Any]
    supplier_result: dict[str, Any]
    analysis_result: dict[str, Any]

    # Validation
    validation_status: Literal["pending", "approved", "needs_revision"]
    validation_feedback: list[str]
    revision_count: int
    max_revisions: int

    # Final response
    final_response: dict[str, Any] | None

    # Shared diagnostics
    errors: Annotated[list[str], add]
    execution_log: Annotated[list[str], add]