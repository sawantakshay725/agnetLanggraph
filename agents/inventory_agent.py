from graph.state import SupplyChainState
from tools.analytics import run_analysis

def inventory_agent(state: SupplyChainState) -> dict:
    try:
        # Build the list of dicts expected by run_analysis
        data = [{
            "product_id": state.get("product_id"),
            "location_id": state.get("location_id"),
            "stock_level": state.get("stock_level", 0),
            "safety_stock": state.get("safety_stock", 0),
        }]

        result = run_analysis(data)

        return {
            "inventory_result": result,
            "execution_log": ["Inventory analysis completed"],
        }
    except Exception as exc:
        return {
            "inventory_result": {},
            "errors": [f"Inventory agent failed: {exc}"],
        }
