import pandas as pd
from graph.state import SupplyChainState
from graph.graph import supply_chain_graph

def run_csv_analysis(file_path: str):
    df = pd.read_csv(file_path)

    results = []
    for _, row in df.iterrows():
        state = SupplyChainState(
            product_id=row.get("product_id"),
            location_id=row.get("location_id"),
            stock_level=row.get("stock_level", 0),
            safety_stock=row.get("safety_stock", 0),
            supplier_id=row.get("supplier_id"),
            reliability_score=row.get("reliability_score", 0),
            lead_time=row.get("lead_time", 0),
            forecast_horizon=row.get("forecast_horizon", 30),
        )
        result = supply_chain_graph.invoke(state)
        results.append(result["final_response"])

    return results

if __name__ == "__main__":
    output = run_csv_analysis("data/dummy_data.csv")
    for i, res in enumerate(output, 1):
        print(f"Row {i} result:\n{res}\n")
