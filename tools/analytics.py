import statistics
from typing import Any, Dict, List


def analyze_inventory(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Perform basic analytics on inventory data.
    Expected input: list of dicts with keys like 'product_id', 'stock_level', 'safety_stock', 'location_id'.
    """

    if not data:
        return {"summary": "No inventory data provided", "alerts": []}

    stock_levels = [item.get("stock_level", 0) for item in data]
    safety_stocks = [item.get("safety_stock", 0) for item in data]

    avg_stock = statistics.mean(stock_levels) if stock_levels else 0
    avg_safety = statistics.mean(safety_stocks) if safety_stocks else 0

    alerts = []
    for item in data:
        if item.get("stock_level", 0) < item.get("safety_stock", 0):
            alerts.append(
                f"Product {item.get('product_id')} at location {item.get('location_id')} is below safety stock."
            )

    return {
        "summary": {
            "average_stock_level": avg_stock,
            "average_safety_stock": avg_safety,
            "total_products": len(data),
        },
        "alerts": alerts,
        "recommendations": [
            "Review products with stock below safety levels.",
            "Consider adjusting reorder points for high-risk items.",
        ],
    }

def analyze_supplier(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Perform basic analytics on supplier data.
    Expected input: list of dicts with keys like 'supplier_id', 'product_id', 'reliability_score', 'lead_time'.
    """

    if not data:
        return {"summary": "No supplier data provided", "alerts": []}

    reliability_scores = [item.get("reliability_score", 0) for item in data]
    lead_times = [item.get("lead_time", 0) for item in data]

    avg_reliability = statistics.mean(reliability_scores) if reliability_scores else 0
    avg_lead_time = statistics.mean(lead_times) if lead_times else 0

    alerts = []
    for item in data:
        if item.get("reliability_score", 0) < 50:
            alerts.append(
                f"Supplier {item.get('supplier_id')} for product {item.get('product_id')} has low reliability."
            )
        if item.get("lead_time", 0) > 30:
            alerts.append(
                f"Supplier {item.get('supplier_id')} has long lead time ({item.get('lead_time')} days)."
            )

    return {
        "summary": {
            "average_reliability_score": avg_reliability,
            "average_lead_time": avg_lead_time,
            "total_suppliers": len(data),
        },
        "alerts": alerts,
        "recommendations": [
            "Review suppliers with low reliability scores.",
            "Negotiate better lead times with slow suppliers.",
        ],
    }

def run_analysis(data: Any) -> Dict[str, Any]:
    """
    General analytics entry point.
    Routes to inventory or supplier analysis depending on input.
    """
    if isinstance(data, list) and all(isinstance(d, dict) for d in data):
        # Decide based on keys present
        if "stock_level" in data[0]:
            return analyze_inventory(data)
        elif "supplier_id" in data[0]:
            return analyze_supplier(data)

    return {"summary": f"Generic analytics summary: {data}", "alerts": []}

