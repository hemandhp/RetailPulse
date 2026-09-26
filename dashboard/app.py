import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="RetailPulse",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Project paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "processed"

# -----------------------------
# Load project data
# -----------------------------

clean_data = pd.read_csv(DATA_DIR / "retail_clean.csv")
customer_segments = pd.read_csv(DATA_DIR / "customer_segments.csv")
churn_predictions = pd.read_csv(DATA_DIR / "churn_predictions.csv")
inventory = pd.read_csv(DATA_DIR / "inventory_recommendations.csv")
daily_revenue = pd.read_csv(DATA_DIR / "daily_revenue.csv")

daily_revenue["InvoiceDate"] = pd.to_datetime(
    daily_revenue["InvoiceDate"]
)
# -----------------------------
# Dashboard header
# -----------------------------

st.title("📊 RetailPulse")
st.subheader("AI-Powered Customer Analytics & Demand Forecasting Platform")

st.markdown(
    "A unified dashboard for customer analytics, demand forecasting, "
    "churn prediction, and inventory optimization."
)

# -----------------------------
# KPI calculations
# -----------------------------

total_transactions = len(clean_data)
total_customers = customer_segments["CustomerID"].nunique()
total_products = inventory["StockCode"].nunique()
high_churn_customers = (
    churn_predictions["RiskLevel"] == "High"
).sum()

# -----------------------------
# KPI cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Transactions", f"{total_transactions:,}")

with col2:
    st.metric("Customers", f"{total_customers:,}")

with col3:
    st.metric("Products", f"{total_products:,}")

with col4:
    st.metric("High Churn Risk", f"{high_churn_customers:,}")

st.divider()

# -----------------------------
# Customer Segmentation
# -----------------------------

st.header("👥 Customer Segmentation")

segment_counts = (
    customer_segments["Segment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = ["Segment", "Customers"]

st.bar_chart(
    segment_counts.set_index("Segment")
)

st.dataframe(
    segment_counts,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Demand Forecasting
# -----------------------------

st.header("📈 Demand Forecasting")

st.markdown(
    "Daily revenue trend used for demand forecasting."
)

st.line_chart(
    daily_revenue.set_index("InvoiceDate")["TotalRevenue"]
)

st.subheader("Recent Revenue")

st.dataframe(
    daily_revenue.tail(30),
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Churn Prediction
# -----------------------------

st.header("⚠️ Customer Churn Prediction")

risk_counts = (
    churn_predictions["RiskLevel"]
    .value_counts()
    .reindex(["Low", "Medium", "High"])
    .fillna(0)
    .astype(int)
    .reset_index()
)

risk_counts.columns = ["RiskLevel", "Customers"]

st.bar_chart(
    risk_counts.set_index("RiskLevel")
)

st.subheader("Churn Risk Distribution")

st.dataframe(
    risk_counts,
    use_container_width=True,
    hide_index=True
)

st.subheader("Top 10 High-Risk Customers")

top_risk_customers = churn_predictions[
    ["CustomerID", "ChurnProbability", "RiskLevel"]
].head(10)

st.dataframe(
    top_risk_customers,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Inventory Optimization
# -----------------------------

st.header("📦 Inventory Optimization")

priority_counts = (
    inventory["InventoryPriority"]
    .value_counts()
    .reindex(["Low", "Medium", "High"])
    .fillna(0)
    .astype(int)
    .reset_index()
)

priority_counts.columns = ["InventoryPriority", "Products"]

st.bar_chart(
    priority_counts.set_index("InventoryPriority")
)

st.subheader("Inventory Priority Distribution")

st.dataframe(
    priority_counts,
    use_container_width=True,
    hide_index=True
)

st.subheader("Top 15 Products Requiring Inventory Attention")

top_inventory = inventory[
    [
        "StockCode",
        "Description",
        "AverageDailyDemand",
        "SafetyStock",
        "ReorderPoint",
        "InventoryPriority"
    ]
].head(15)

st.dataframe(
    top_inventory,
    use_container_width=True,
    hide_index=True
)

st.success("RetailPulse Dashboard loaded successfully!")