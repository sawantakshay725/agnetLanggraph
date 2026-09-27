from graph.state import SupplyChainState
from tools.analytics import analyze_supplier

def supplier_agent(state: SupplyChainState) -> dict:
    try:
        data = [{
            "supplier_id": state.get("supplier_id"),
            "product_id": state.get("product_id"),
            "reliability_score": state.get("reliability_score", 0),
            "lead_time": state.get("lead_time", 0),
        }]
        result = analyze_supplier(data)

        return {
            "supplier_result": result,
            "execution_log": ["Supplier analysis completed"],
        }
    except Exception as exc:
        return {
            "supplier_result": {},
            "errors": [f"Supplier agent failed: {exc}"],
        }
