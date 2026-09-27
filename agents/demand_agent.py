from graph.state import SupplyChainState
from tools.forecasting import forecast_demand


def demand_agent(state: SupplyChainState) -> dict:
    try:
        result = forecast_demand(
            product_id=state.get("product_id"),
            horizon=state.get("forecast_horizon", 30),
        )

        return {
            "demand_result": result,
            "execution_log": ["Demand analysis completed"],
        }
    except Exception as exc:
        return {
            "demand_result": {},
            "errors": [f"Demand agent failed: {exc}"],
        }