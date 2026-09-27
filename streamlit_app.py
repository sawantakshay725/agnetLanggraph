import streamlit as st
import pandas as pd
from openai import OpenAI

from graph.graph import supply_chain_graph
from graph.state import SupplyChainState
from config import get_config

# Load config
config = get_config()

st.title("Supply Chain Intelligence")

query = st.selectbox(
    "What would you like to analyze?",
    ["inventory", "supplier", "demand"]
)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

forecast_horizon = st.number_input(
    "Forecast horizon (days)",
    min_value=1,
    max_value=365,
    value=config.DEFAULT_FORECAST_HORIZON,
)

if uploaded_file and st.button("Run analysis"):
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:", df.head())

    results = []
    with st.spinner("Running supply-chain agents..."):
        for _, row in df.iterrows():
            initial_state = {
                "query": query,
                "product_id": row.get("product_id"),
                "location_id": row.get("location_id"),
                "stock_level": row.get("stock_level", 0),
                "safety_stock": row.get("safety_stock", 0),
                "supplier_id": row.get("supplier_id"),
                "reliability_score": row.get("reliability_score", 0),
                "lead_time": row.get("lead_time", 0),
                "forecast_horizon": int(forecast_horizon),
                "validation_status": "pending",
                "validation_feedback": [],
                "revision_count": 0,
                "max_revisions": 2,
                "errors": [],
                "execution_log": [],
            }

            result = supply_chain_graph.invoke(initial_state)
            results.append(result.get("final_response"))

    # --- Summarize with DeepSeek ---
    deepseek_client = OpenAI(
        api_key=config.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )

    summary_prompt = f"""
    You are a supply chain analyst. Summarize the following JSON results into a clear,
    structured report with sections for Key Metrics, Alerts, and Recommendations:

    {results}
    """

    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": summary_prompt}],
        max_tokens=600,
    )

    st.subheader("LLM Summary (DeepSeek)")
    st.write(response.choices[0].message.content)
