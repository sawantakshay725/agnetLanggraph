import statistics
from typing import Any, Dict, List


def forecast_demand(data: List[Dict[str, Any]], horizon: int = 30) -> Dict[str, Any]:
    """
    Forecast demand based on historical sales data.

    Args:
        data: List of records, each containing 'date' and 'sales' keys.
        horizon: Number of future periods to forecast (default = 30).

    Returns:
        A dictionary with forecast values, confidence intervals, and summary stats.
    """

    if not data:
        return {"forecast": [], "summary": "No historical data provided"}

    # Extract sales values
    sales = [record.get("sales", 0) for record in data]

    # Basic statistics
    avg_sales = statistics.mean(sales)
    stdev_sales = statistics.pstdev(sales) if len(sales) > 1 else 0

    # Naive forecast: repeat average sales for horizon
    forecast = [avg_sales for _ in range(horizon)]

    return {
        "forecast": forecast,
        "summary": {
            "historical_records": len(data),
            "average_sales": avg_sales,
            "sales_stdev": stdev_sales,
            "forecast_horizon": horizon,
        },
        "confidence_interval": {
            "lower_bound": avg_sales - stdev_sales,
            "upper_bound": avg_sales + stdev_sales,
        },
        "recommendations": [
            "Consider seasonality adjustments for more accurate forecasts.",
            "Use ML models for advanced demand prediction."
        ],
    }
