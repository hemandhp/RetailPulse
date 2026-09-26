import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="RetailPulse",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# RETAILPULSE LOGIN
# ==========================================

def login_page():

    st.markdown(
        """
        <style>
        .login-container {
            max-width: 430px;
            margin: 100px auto 0 auto;
            padding: 40px;
            background: #15161E;
            border: 1px solid #2A2B35;
            border-radius: 20px;
            text-align: center;
        }

        .login-logo {
            width: 70px;
            height: 70px;
            margin: 0 auto 20px auto;
            border-radius: 18px;
            background: #6254D9;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 34px;
        }

        .login-title {
            color: #FFFFFF;
            font-size: 30px;
            font-weight: 750;
            margin-bottom: 5px;
        }

        .login-subtitle {
            color: #9997AA;
            font-size: 13px;
            margin-bottom: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="login-container">
            <div class="login-logo">📊</div>
            <div class="login-title">RetailPulse</div>
            <div class="login-subtitle">
                AI-Powered Customer Analytics
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    login_clicked = st.button(
        "🔐  Login",
        use_container_width=True
    )

    if login_clicked:

        correct_email = st.secrets["login"]["email"]
        correct_password = st.secrets["login"]["password"]

        if email == correct_email and password == correct_password:
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email
            st.rerun()

        else:
            st.error("Invalid email or password.")

    st.caption(
        "Use your authorized RetailPulse account to continue."
    )


    # ==========================================
# AUTHENTICATION CHECK
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:

    login_page()

    st.stop()

    



st.markdown(
    """
    <style>
    .main {
        padding-top: 1rem;
    }

    [data-testid="stMetric"] {
        border: 1px solid rgba(128, 128, 128, 0.25);
        border-radius: 10px;
        padding: 15px;
    }

    h1 {
        font-weight: 700;
    }

    h2, h3 {
        font-weight: 600;
    }

   /* ==========================================
       RETAILPULSE DARK THEME
    ========================================== */

   .stApp {
    background: var(--background-color) !important;
}

.main {
    background: var(--background-color) !important;
    color: var(--text-color) !important;
    padding-top: 1rem;
}

/* Main text */
.main p,
.main span,
.main label {
    color: var(--text-color);
}

/* Headings */
h1, h2, h3, h4 {
    color: var(--text-color) !important;
}

    /* ==========================================
       SIDEBAR
    ========================================== */

    [data-testid="stSidebar"] {
        background: #11121A !important;
        border-right: 1px solid #292A35;
    }

    [data-testid="stSidebar"] > div:first-child {
        background: #11121A !important;
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* ==========================================
       BRAND
    ========================================== */

    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 8px 22px 8px;
    }

    .brand-icon {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: #6254D9;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 21px;
        color: #FFFFFF !important;

        box-shadow: 0 5px 18px rgba(98, 84, 217, 0.30);
    }

    .brand-name {
        font-size: 19px;
        font-weight: 750;
        color: #FFFFFF !important;
    }

    .brand-subtitle {
        font-size: 10px;
        color: #9997AA !important;
    }

    /* ==========================================
       SECTION TITLE
    ========================================== */

    .nav-section {
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.2px;
        color: #777587 !important;
        margin: 12px 8px 8px 8px;
    }

    /* ==========================================
       NAVIGATION
    ========================================== */

    [data-testid="stSidebar"] [data-testid="stRadio"] > div {
        gap: 4px;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        border-radius: 9px;
        padding: 10px;
        margin: 2px 0;

        color: #B7B5C7 !important;

        font-size: 13px;
        font-weight: 550;

        transition: all 0.15s ease;
    }

    /* Hover */

    [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
        background: #1D1B35 !important;
        color: #FFFFFF !important;
    }

    /* Active */

    [data-testid="stSidebar"]
    [data-testid="stRadio"]
    label:has(input:checked) {

        background: #252144 !important;

        color: #9B91FF !important;

        font-weight: 700;

        box-shadow: inset 3px 0 0 #7567E8;
    }

    [data-testid="stSidebar"]
    [data-testid="stRadio"]
    label:has(input:checked) p {
        color: #9B91FF !important;
    }

    /* Hide radio circles */

    [data-testid="stSidebar"] [data-testid="stRadio"] input {
        display: none;
    }

    /* ==========================================
       KPI CARDS
    ========================================== */

    [data-testid="stMetric"] {

        background: #15161E !important;

        border: 1px solid #2A2B35 !important;

        border-radius: 12px !important;

        padding: 18px !important;

        box-shadow: none;
    }

    [data-testid="stMetricLabel"] {
        color: #AAA8B8 !important;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    /* ==========================================
       TABLES
    ========================================== */

    [data-testid="stDataFrame"] {
        background: #15161E !important;
        border: 1px solid #2A2B35 !important;
        border-radius: 12px;
    }

    /* ==========================================
       SELECTBOX
    ========================================== */

    [data-baseweb="select"] > div {
        background: #15161E !important;
        border-color: #30313D !important;
        color: #FFFFFF !important;
        border-radius: 9px !important;
    }

    /* ==========================================
       BUTTONS
    ========================================== */

    .stButton > button {

        background: #6254D9 !important;

        color: #FFFFFF !important;

        border: none !important;

        border-radius: 9px !important;

        font-weight: 600;
    }

    .stButton > button:hover {
        background: #7567E8 !important;
    }

    /* ==========================================
       PROJECT CARD
    ========================================== */

    .sidebar-info {

        background: #181923;

        border: 1px solid #2A2B35;

        border-radius: 12px;

        padding: 13px;

        margin: 8px 4px;
    }

    .info-title {
        color: #FFFFFF !important;
        font-size: 13px;
        font-weight: 700;
    }

    .info-text {
        color: #9694A7 !important;
        font-size: 11px;
        line-height: 1.5;
        margin-top: 5px;
    }

    /* ==========================================
       STATUS
    ========================================== */

    .sidebar-status {

        display: flex;

        align-items: center;

        gap: 8px;

        padding: 9px 10px;

        color: #9694A7 !important;

        font-size: 11px;
    }

    .status-dot {

        width: 8px;

        height: 8px;

        border-radius: 50%;

        background: #45C77A;

        box-shadow: 0 0 0 3px rgba(69, 199, 122, 0.15);
    }

    /* ==========================================
       FOOTER
    ========================================== */

    .sidebar-footer {

        display: flex;

        align-items: center;

        gap: 10px;

        background: #19172F;

        color: #FFFFFF !important;

        border-radius: 12px;

        padding: 12px;

        margin: 18px 2px 4px 2px;

        border: 1px solid #2B284A;
    }

    .footer-icon {

        width: 30px;

        height: 30px;

        border-radius: 8px;

        background: #6254D9;

        display: flex;

        align-items: center;

        justify-content: center;
    }

    .footer-title {

        font-size: 11px;

        font-weight: 700;

        color: #FFFFFF !important;
    }

    .footer-text {

        font-size: 9px;

        color: #AAA7C2 !important;
    }

    /* ==========================================
       DIVIDERS
    ========================================== */

    hr {
        border-color: #2A2B35 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "processed"

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

clean_data = pd.read_csv(DATA_DIR / "retail_clean.csv")
customer_segments = pd.read_csv(DATA_DIR / "customer_segments.csv")
churn_predictions = pd.read_csv(DATA_DIR / "churn_predictions.csv")
inventory = pd.read_csv(DATA_DIR / "inventory_recommendations.csv")
daily_revenue = pd.read_csv(DATA_DIR / "daily_revenue.csv")

daily_revenue["InvoiceDate"] = pd.to_datetime(
    daily_revenue["InvoiceDate"]
)

# --------------------------------------------------
# RETAILPULSE SIDEBAR
# --------------------------------------------------

st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <div class="brand-icon">📊</div>
        <div>
            <div class="brand-name">RetailPulse</div>
            <div class="brand-subtitle">AI Customer Analytics</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="nav-section">MAIN</div>',
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Dashboard Navigation",
    [
        "🏠  Executive Summary",
        "📈  Sales Trend Analysis",
        "📦  Product Performance",
        "👥  Customer Analytics",
        "🌍  Region/Country Sales",
        "📅  Monthly & Seasonal Sales",
        "🧠  Customer Behaviour",
        "💰  Revenue Analysis",
        "🚨  Inventory Risk",
        "🧾  Order & Transaction",
        "🤖  Advanced Analytics",
        "🎛️  Interactive Filters"
    ],
    label_visibility="collapsed"
)

# Remove icons before page comparison
page = page.split("  ", 1)[1]

st.sidebar.markdown(
    '<div class="nav-section">PROJECT</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div class="sidebar-info">
        <div class="info-title">RetailPulse</div>
        <div class="info-text">
            AI-powered customer analytics,
            demand forecasting and inventory insights.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <div class="sidebar-status">
        <span class="status-dot"></span>
        <span>Analytics system active</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div class="sidebar-footer">
        <div class="footer-icon">⚡</div>
        <div>
            <div class="footer-title">RetailPulse</div>
            <div class="footer-text">Data Science & Analytics</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

st.sidebar.caption(
    f"Logged in as: {st.session_state.get('user_email', '')}"
)

if st.sidebar.button(
    "🚪 Logout",
    use_container_width=True
):

    st.session_state["logged_in"] = False
    st.session_state.pop("user_email", None)

    st.rerun()



# --------------------------------------------------
# PAGE 1: EXECUTIVE SUMMARY
# --------------------------------------------------

if page == "Executive Summary":

    st.title("📊 RetailPulse")
    st.subheader(
        "AI-Powered Customer Analytics & Demand Forecasting Platform"
    )

    st.markdown(
        "Executive overview of retail transactions, customers, "
        "products, revenue, churn risk, and inventory risk."
    )

    # --------------------------------------------------
    # KPI CALCULATIONS
    # --------------------------------------------------

    total_transactions = len(clean_data)

    total_customers = clean_data["CustomerID"].nunique()

    total_products = clean_data["StockCode"].nunique()

    total_revenue = clean_data["TotalRevenue"].sum()

    high_churn_customers = (
        churn_predictions["RiskLevel"] == "High"
    ).sum()

    high_inventory_products = (
        inventory["InventoryPriority"] == "High"
    ).sum()

    # --------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Transactions",
            f"{total_transactions:,}"
        )

    with col2:
        st.metric(
            "Customers",
            f"{total_customers:,}"
        )

    with col3:
        st.metric(
            "Products",
            f"{total_products:,}"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "Total Revenue",
            f"£{total_revenue:,.0f}"
        )

    with col5:
        st.metric(
            "High Churn Risk",
            f"{high_churn_customers:,}"
        )

    with col6:
        st.metric(
            "High Inventory Risk",
            f"{high_inventory_products:,}"
        )

    st.divider()

    # --------------------------------------------------
    # REVENUE TREND
    # --------------------------------------------------

    st.header("📈 Revenue Trend")

    st.line_chart(
        daily_revenue.set_index("InvoiceDate")["TotalRevenue"]
    )

    # --------------------------------------------------
    # QUICK INSIGHTS
    # --------------------------------------------------

    st.header("🔎 Key Business Indicators")

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:

        st.subheader("👥 Customer Risk")

        risk_counts = (
            churn_predictions["RiskLevel"]
            .value_counts()
            .reindex(["Low", "Medium", "High"])
            .fillna(0)
            .astype(int)
        )

        st.dataframe(
            risk_counts.rename("Customers"),
            use_container_width=True
        )

    with insight_col2:

        st.subheader("📦 Inventory Risk")

        inventory_counts = (
            inventory["InventoryPriority"]
            .value_counts()
            .reindex(["Low", "Medium", "High"])
            .fillna(0)
            .astype(int)
        )

        st.dataframe(
            inventory_counts.rename("Products"),
            use_container_width=True
        )

    st.divider()

    st.caption(
        "RetailPulse | Customer Analytics • Demand Forecasting "
        "• Churn Prediction • Inventory Optimization"
    )

    # --------------------------------------------------
# PAGE 2: SALES TREND ANALYSIS
# --------------------------------------------------

elif page == "Sales Trend Analysis":

    st.title("📈 Sales Trend Analysis")

    st.markdown(
        "Analysis of daily and weekly revenue patterns "
        "using historical retail transaction data."
    )

    # --------------------------------------------------
    # SALES KPIs
    # --------------------------------------------------

    total_revenue = clean_data["TotalRevenue"].sum()

    average_daily_revenue = daily_revenue["TotalRevenue"].mean()

    highest_revenue_day = daily_revenue.loc[
        daily_revenue["TotalRevenue"].idxmax()
    ]

    lowest_revenue_day = daily_revenue.loc[
        daily_revenue["TotalRevenue"].idxmin()
    ]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Revenue",
            f"£{total_revenue:,.0f}"
        )

    with col2:
        st.metric(
            "Average Daily Revenue",
            f"£{average_daily_revenue:,.0f}"
        )

    with col3:
        st.metric(
            "Highest Revenue Day",
            f"£{highest_revenue_day['TotalRevenue']:,.0f}"
        )

    with col4:
        st.metric(
            "Lowest Revenue Day",
            f"£{lowest_revenue_day['TotalRevenue']:,.0f}"
        )

    st.divider()

    # --------------------------------------------------
    # DAILY REVENUE
    # --------------------------------------------------

    st.header("Daily Revenue Trend")

    st.line_chart(
        daily_revenue.set_index("InvoiceDate")["TotalRevenue"]
    )

    # --------------------------------------------------
    # WEEKLY REVENUE
    # --------------------------------------------------

    weekly_revenue = (
        clean_data.assign(
            InvoiceDate=pd.to_datetime(clean_data["InvoiceDate"])
        )
        .set_index("InvoiceDate")
        .resample("W")["TotalRevenue"]
        .sum()
        .reset_index()
    )

    st.header("Weekly Revenue Trend")

    st.line_chart(
        weekly_revenue.set_index("InvoiceDate")["TotalRevenue"]
    )

    # --------------------------------------------------
    # BEST AND WORST DAYS
    # --------------------------------------------------

    st.header("Revenue Extremes")

    best_day = daily_revenue.nlargest(
        10, "TotalRevenue"
    ).copy()

    worst_day = daily_revenue.nsmallest(
        10, "TotalRevenue"
    ).copy()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔝 Top 10 Revenue Days")

        st.dataframe(
            best_day,
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.subheader("⬇️ Lowest 10 Revenue Days")

        st.dataframe(
            worst_day,
            use_container_width=True,
            hide_index=True
        )

        # --------------------------------------------------
# PAGE 3: PRODUCT PERFORMANCE
# --------------------------------------------------

elif page == "Product Performance":

    st.title("📦 Product Performance Dashboard")

    st.markdown(
        "Analyze product sales, revenue, and quantity performance."
    )

    # --------------------------------------------------
    # PRODUCT SUMMARY
    # --------------------------------------------------

    total_products = clean_data["StockCode"].nunique()

    total_quantity = clean_data["Quantity"].sum()

    total_revenue = clean_data["TotalRevenue"].sum()

    average_product_revenue = (
        clean_data.groupby("StockCode")["TotalRevenue"]
        .sum()
        .mean()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Products",
            f"{total_products:,}"
        )

    with col2:
        st.metric(
            "Quantity Sold",
            f"{total_quantity:,}"
        )

    with col3:
        st.metric(
            "Total Revenue",
            f"£{total_revenue:,.0f}"
        )

    with col4:
        st.metric(
            "Avg Product Revenue",
            f"£{average_product_revenue:,.0f}"
        )

    st.divider()

    # --------------------------------------------------
    # PRODUCT AGGREGATION
    # --------------------------------------------------

    product_performance = (
        clean_data.groupby(
            ["StockCode", "Description"],
            dropna=False
        )
        .agg(
            QuantitySold=("Quantity", "sum"),
            Revenue=("TotalRevenue", "sum"),
            AverageUnitPrice=("UnitPrice", "mean")
        )
        .reset_index()
    )

    # --------------------------------------------------
    # TOP PRODUCTS BY REVENUE
    # --------------------------------------------------

    st.header("💰 Top Products by Revenue")

    top_revenue_products = (
        product_performance
        .sort_values("Revenue", ascending=False)
        .head(15)
    )

    st.bar_chart(
        top_revenue_products.set_index(
            "Description"
        )["Revenue"]
    )

    st.dataframe(
        top_revenue_products,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # TOP PRODUCTS BY QUANTITY
    # --------------------------------------------------

    st.header("📊 Top Products by Quantity Sold")

    top_quantity_products = (
        product_performance
        .sort_values("QuantitySold", ascending=False)
        .head(15)
    )

    st.bar_chart(
        top_quantity_products.set_index(
            "Description"
        )["QuantitySold"]
    )

    st.dataframe(
        top_quantity_products,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # PRODUCT PERFORMANCE TABLE
    # --------------------------------------------------

    st.header("🔎 Product Performance Details")

    st.dataframe(
        product_performance.sort_values(
            "Revenue",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
# PAGE 4: CUSTOMER ANALYTICS
# --------------------------------------------------

elif page == "Customer Analytics":

    st.title("👥 Customer Analytics Dashboard")

    st.markdown(
        "Analyze customer value, purchasing behaviour, "
        "and RFM-based customer segments."
    )

    # --------------------------------------------------
    # CUSTOMER KPIs
    # --------------------------------------------------

    total_customers = customer_segments["CustomerID"].nunique()

    average_recency = customer_segments["Recency"].mean()

    average_frequency = customer_segments["Frequency"].mean()

    average_monetary = customer_segments["Monetary"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Customers",
            f"{total_customers:,}"
        )

    with col2:
        st.metric(
            "Avg Recency",
            f"{average_recency:.1f} days"
        )

    with col3:
        st.metric(
            "Avg Frequency",
            f"{average_frequency:.1f}"
        )

    with col4:
        st.metric(
            "Avg Monetary Value",
            f"£{average_monetary:,.0f}"
        )

    st.divider()

    # --------------------------------------------------
    # CUSTOMER SEGMENTS
    # --------------------------------------------------

    st.header("🎯 Customer Segment Distribution")

    segment_counts = (
        customer_segments["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = [
        "Segment",
        "Customers"
    ]

    st.bar_chart(
        segment_counts.set_index("Segment")
    )

    st.dataframe(
        segment_counts,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # SEGMENT RFM ANALYSIS
    # --------------------------------------------------

    st.header("📊 Segment RFM Analysis")

    segment_rfm = (
        customer_segments
        .groupby("Segment")
        .agg(
            Customers=("CustomerID", "nunique"),
            AvgRecency=("Recency", "mean"),
            AvgFrequency=("Frequency", "mean"),
            AvgMonetary=("Monetary", "mean")
        )
        .reset_index()
    )

    segment_rfm["AvgRecency"] = (
        segment_rfm["AvgRecency"].round(1)
    )

    segment_rfm["AvgFrequency"] = (
        segment_rfm["AvgFrequency"].round(1)
    )

    segment_rfm["AvgMonetary"] = (
        segment_rfm["AvgMonetary"].round(2)
    )

    st.dataframe(
        segment_rfm,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # CUSTOMER DETAILS
    # --------------------------------------------------

    st.header("🔎 Customer Segment Details")

    selected_segment = st.selectbox(
        "Select a customer segment",
        ["All"] +
        sorted(
            customer_segments["Segment"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    if selected_segment == "All":
        filtered_customers = customer_segments
    else:
        filtered_customers = customer_segments[
            customer_segments["Segment"] == selected_segment
        ]

    st.dataframe(
        filtered_customers,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
# PAGE 5: REGION / COUNTRY SALES
# --------------------------------------------------

elif page == "Region/Country Sales":

    st.title("🌍 Region / Country Sales Dashboard")

    st.markdown(
        "Analyze sales performance, transactions, and customer "
        "distribution across countries."
    )

    # --------------------------------------------------
    # COUNTRY KPIs
    # --------------------------------------------------

    total_countries = clean_data["Country"].nunique()

    total_revenue = clean_data["TotalRevenue"].sum()

    top_country = (
        clean_data.groupby("Country")["TotalRevenue"]
        .sum()
        .idxmax()
    )

    top_country_revenue = (
        clean_data.groupby("Country")["TotalRevenue"]
        .sum()
        .max()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Countries",
            f"{total_countries:,}"
        )

    with col2:
        st.metric(
            "Total Revenue",
            f"£{total_revenue:,.0f}"
        )

    with col3:
        st.metric(
            "Top Country",
            top_country
        )

    with col4:
        st.metric(
            "Top Country Revenue",
            f"£{top_country_revenue:,.0f}"
        )

    st.divider()

    # --------------------------------------------------
    # COUNTRY SALES SUMMARY
    # --------------------------------------------------

    country_sales = (
        clean_data.groupby("Country")
        .agg(
            Revenue=("TotalRevenue", "sum"),
            Transactions=("InvoiceNo", "nunique"),
            Customers=("CustomerID", "nunique"),
            QuantitySold=("Quantity", "sum")
        )
        .reset_index()
    )

    country_sales = country_sales.sort_values(
        "Revenue",
        ascending=False
    )

    # --------------------------------------------------
    # TOP COUNTRIES BY REVENUE
    # --------------------------------------------------

    st.header("💰 Top 15 Countries by Revenue")

    top_countries = country_sales.head(15)

    st.bar_chart(
        top_countries.set_index("Country")["Revenue"]
    )

    st.dataframe(
        top_countries,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # TRANSACTIONS BY COUNTRY
    # --------------------------------------------------

    st.header("🧾 Transactions by Country")

    top_transaction_countries = (
        country_sales
        .sort_values(
            "Transactions",
            ascending=False
        )
        .head(15)
    )

    st.bar_chart(
        top_transaction_countries.set_index(
            "Country"
        )["Transactions"]
    )

    # --------------------------------------------------
    # CUSTOMERS BY COUNTRY
    # --------------------------------------------------

    st.header("👥 Customers by Country")

    top_customer_countries = (
        country_sales
        .sort_values(
            "Customers",
            ascending=False
        )
        .head(15)
    )

    st.bar_chart(
        top_customer_countries.set_index(
            "Country"
        )["Customers"]
    )

    # --------------------------------------------------
    # COMPLETE COUNTRY TABLE
    # --------------------------------------------------

    st.header("🔎 Country Sales Details")

    st.dataframe(
        country_sales,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
# PAGE 6: MONTHLY & SEASONAL SALES
# --------------------------------------------------

elif page == "Monthly & Seasonal Sales":

    st.title("📅 Monthly & Seasonal Sales Dashboard")

    st.markdown(
        "Analyze monthly revenue, transaction activity, "
        "and seasonal sales patterns."
    )

    # --------------------------------------------------
    # PREPARE DATE DATA
    # --------------------------------------------------

    sales_data = clean_data.copy()

    sales_data["InvoiceDate"] = pd.to_datetime(
        sales_data["InvoiceDate"]
    )

    sales_data["Year"] = sales_data["InvoiceDate"].dt.year

    sales_data["Month"] = sales_data["InvoiceDate"].dt.month

    sales_data["MonthName"] = (
        sales_data["InvoiceDate"]
        .dt.month_name()
    )

    # --------------------------------------------------
    # MONTHLY SUMMARY
    # --------------------------------------------------

    monthly_sales = (
        sales_data
        .groupby(["Year", "Month", "MonthName"])
        .agg(
            Revenue=("TotalRevenue", "sum"),
            Transactions=("InvoiceNo", "nunique"),
            QuantitySold=("Quantity", "sum"),
            Customers=("CustomerID", "nunique")
        )
        .reset_index()
    )

    monthly_sales = monthly_sales.sort_values(
        ["Year", "Month"]
    )

    monthly_sales["Period"] = (
        monthly_sales["MonthName"]
        + " "
        + monthly_sales["Year"].astype(str)
    )

    # --------------------------------------------------
    # KPI VALUES
    # --------------------------------------------------

    total_revenue = monthly_sales["Revenue"].sum()

    average_monthly_revenue = (
        monthly_sales["Revenue"].mean()
    )

    highest_month = monthly_sales.loc[
        monthly_sales["Revenue"].idxmax()
    ]

    total_months = len(monthly_sales)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Revenue",
            f"£{total_revenue:,.0f}"
        )

    with col2:
        st.metric(
            "Avg Monthly Revenue",
            f"£{average_monthly_revenue:,.0f}"
        )

    with col3:
        st.metric(
            "Highest Revenue Month",
            highest_month["Period"]
        )

    with col4:
        st.metric(
            "Periods Analyzed",
            f"{total_months:,}"
        )

    st.divider()

    # --------------------------------------------------
    # MONTHLY REVENUE TREND
    # --------------------------------------------------

    st.header("📈 Monthly Revenue Trend")

    st.line_chart(
        monthly_sales.set_index("Period")["Revenue"]
    )

    # --------------------------------------------------
    # MONTHLY TRANSACTIONS
    # --------------------------------------------------

    st.header("🧾 Monthly Transaction Volume")

    st.bar_chart(
        monthly_sales.set_index("Period")["Transactions"]
    )

    # --------------------------------------------------
    # SEASONAL MONTH ANALYSIS
    # --------------------------------------------------

    st.header("🌦️ Seasonal Sales Pattern")

    seasonal_sales = (
        sales_data
        .groupby("Month")
        .agg(
            Revenue=("TotalRevenue", "sum"),
            Transactions=("InvoiceNo", "nunique"),
            QuantitySold=("Quantity", "sum"),
            Customers=("CustomerID", "nunique")
        )
        .reset_index()
    )

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    seasonal_sales["MonthName"] = (
        seasonal_sales["Month"]
        .map(month_names)
    )

    seasonal_sales = seasonal_sales.sort_values(
        "Month"
    )

    st.line_chart(
        seasonal_sales.set_index(
            "MonthName"
        )["Revenue"]
    )

    # --------------------------------------------------
    # MONTHLY SALES TABLE
    # --------------------------------------------------

    st.header("🔎 Monthly Sales Details")

    st.dataframe(
        monthly_sales[
            [
                "Period",
                "Revenue",
                "Transactions",
                "QuantitySold",
                "Customers"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # SEASONAL TABLE
    # --------------------------------------------------

    st.header("📊 Seasonal Summary")

    st.dataframe(
        seasonal_sales[
            [
                "MonthName",
                "Revenue",
                "Transactions",
                "QuantitySold",
                "Customers"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
# PAGE 7: CUSTOMER BEHAVIOUR
# --------------------------------------------------

elif page == "Customer Behaviour":

    st.title("🧠 Customer Behaviour Dashboard")

    st.markdown(
        "Analyze customer purchasing frequency, spending patterns, "
        "order behaviour, and recency."
    )

    # --------------------------------------------------
    # CUSTOMER ORDER DATA
    # --------------------------------------------------

    customer_behavior = (
        clean_data.groupby("CustomerID")
        .agg(
            Orders=("InvoiceNo", "nunique"),
            TotalQuantity=("Quantity", "sum"),
            TotalRevenue=("TotalRevenue", "sum"),
            AverageOrderValue=("TotalRevenue", "mean"),
            UniqueProducts=("StockCode", "nunique")
        )
        .reset_index()
    )

    # --------------------------------------------------
    # BEHAVIOUR KPIs
    # --------------------------------------------------

    total_customers = len(customer_behavior)

    average_orders = customer_behavior["Orders"].mean()

    average_order_value = (
        customer_behavior["AverageOrderValue"].mean()
    )

    average_customer_revenue = (
        customer_behavior["TotalRevenue"].mean()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Customers",
            f"{total_customers:,}"
        )

    with col2:
        st.metric(
            "Avg Orders / Customer",
            f"{average_orders:.1f}"
        )

    with col3:
        st.metric(
            "Avg Order Value",
            f"£{average_order_value:,.2f}"
        )

    with col4:
        st.metric(
            "Avg Customer Revenue",
            f"£{average_customer_revenue:,.2f}"
        )

    st.divider()

    # --------------------------------------------------
    # PURCHASE FREQUENCY
    # --------------------------------------------------

    st.header("🛒 Customer Purchase Frequency")

    st.bar_chart(
        customer_behavior["Orders"]
        .value_counts()
        .sort_index()
        .head(20)
    )

    # --------------------------------------------------
    # CUSTOMER SPENDING
    # --------------------------------------------------

    st.header("💰 Customer Spending Distribution")

    spending_bins = pd.cut(
        customer_behavior["TotalRevenue"],
        bins=[
            0,
            100,
            500,
            1000,
            5000,
            10000,
            float("inf")
        ],
        labels=[
            "£0–£100",
            "£100–£500",
            "£500–£1,000",
            "£1,000–£5,000",
            "£5,000–£10,000",
            "£10,000+"
        ]
    )

    spending_distribution = (
        spending_bins
        .value_counts()
        .sort_index()
    )

    st.bar_chart(
        spending_distribution
    )

    # --------------------------------------------------
    # CUSTOMER RECENCY
    # --------------------------------------------------

    st.header("⏱️ Customer Recency")

    recency_distribution = (
        customer_segments["Recency"]
        .clip(upper=180)
        .value_counts()
        .sort_index()
    )

    st.line_chart(
        recency_distribution
    )

    # --------------------------------------------------
    # CUSTOMER BEHAVIOUR TABLE
    # --------------------------------------------------

    st.header("🔎 Customer Behaviour Details")

    top_customers = (
        customer_behavior
        .sort_values(
            "TotalRevenue",
            ascending=False
        )
        .head(50)
    )

    st.dataframe(
        top_customers,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
# PAGE 8: REVENUE ANALYSIS
# --------------------------------------------------

elif page == "Revenue Analysis":

    st.title("💰 Revenue Analysis Dashboard")

    st.markdown(
        "Analyze revenue generation across transactions, "
        "products, and countries."
    )

    # --------------------------------------------------
    # REVENUE KPIs
    # --------------------------------------------------

    total_revenue = clean_data["TotalRevenue"].sum()

    average_transaction_revenue = (
        clean_data["TotalRevenue"].mean()
    )

    average_unit_price = (
        clean_data["UnitPrice"].mean()
    )

    revenue_per_customer = (
        total_revenue /
        clean_data["CustomerID"].nunique()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Revenue",
            f"£{total_revenue:,.0f}"
        )

    with col2:
        st.metric(
            "Avg Transaction Revenue",
            f"£{average_transaction_revenue:,.2f}"
        )

    with col3:
        st.metric(
            "Avg Unit Price",
            f"£{average_unit_price:,.2f}"
        )

    with col4:
        st.metric(
            "Revenue / Customer",
            f"£{revenue_per_customer:,.2f}"
        )

    st.divider()

    # --------------------------------------------------
    # REVENUE TREND
    # --------------------------------------------------

    st.header("📈 Revenue Trend")

    st.line_chart(
        daily_revenue.set_index("InvoiceDate")[
            "TotalRevenue"
        ]
    )

    # --------------------------------------------------
    # REVENUE BY COUNTRY
    # --------------------------------------------------

    st.header("🌍 Revenue by Country")

    country_revenue = (
        clean_data
        .groupby("Country")["TotalRevenue"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
    )

    st.bar_chart(country_revenue)

    # --------------------------------------------------
    # REVENUE BY PRODUCT
    # --------------------------------------------------

    st.header("📦 Top Products by Revenue")

    product_revenue = (
        clean_data
        .groupby("Description")["TotalRevenue"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
    )

    st.bar_chart(product_revenue)

    # --------------------------------------------------
    # REVENUE CONCENTRATION
    # --------------------------------------------------

    st.header("📊 Revenue Concentration")

    product_revenue_all = (
        clean_data
        .groupby("StockCode")["TotalRevenue"]
        .sum()
        .sort_values(ascending=False)
    )

    total_product_revenue = product_revenue_all.sum()

    top_10_revenue = (
        product_revenue_all.head(10).sum()
    )

    top_50_revenue = (
        product_revenue_all.head(50).sum()
    )

    top_10_percentage = (
        top_10_revenue /
        total_product_revenue
        * 100
    )

    top_50_percentage = (
        top_50_revenue /
        total_product_revenue
        * 100
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Top 10 Products Revenue Share",
            f"{top_10_percentage:.1f}%"
        )

    with col2:
        st.metric(
            "Top 50 Products Revenue Share",
            f"{top_50_percentage:.1f}%"
        )

    # --------------------------------------------------
    # REVENUE NOTE
    # --------------------------------------------------

    st.info(
        "Profit is not calculated because the dataset does not "
        "contain product cost information. This dashboard therefore "
        "reports revenue and revenue-related metrics only."
    )

    # --------------------------------------------------
# PAGE 9: INVENTORY RISK
# --------------------------------------------------

elif page == "Inventory Risk":

    st.title("📦 Inventory Risk Dashboard")

    st.markdown(
        "Identify products requiring inventory attention "
        "using demand, safety stock, and reorder-point analysis."
    )

    # --------------------------------------------------
    # INVENTORY KPIs
    # --------------------------------------------------

    total_products = inventory["StockCode"].nunique()

    high_priority = (
        inventory["InventoryPriority"] == "High"
    ).sum()

    medium_priority = (
        inventory["InventoryPriority"] == "Medium"
    ).sum()

    low_priority = (
        inventory["InventoryPriority"] == "Low"
    ).sum()

    average_daily_demand = (
        inventory["AverageDailyDemand"].mean()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Products Analyzed",
            f"{total_products:,}"
        )

    with col2:
        st.metric(
            "High Priority",
            f"{high_priority:,}"
        )

    with col3:
        st.metric(
            "Medium Priority",
            f"{medium_priority:,}"
        )

    with col4:
        st.metric(
            "Avg Daily Demand",
            f"{average_daily_demand:,.2f}"
        )

    st.divider()

    # --------------------------------------------------
    # PRIORITY DISTRIBUTION
    # --------------------------------------------------

    st.header("🚨 Inventory Priority Distribution")

    priority_counts = (
        inventory["InventoryPriority"]
        .value_counts()
        .reindex(["Low", "Medium", "High"])
        .fillna(0)
        .astype(int)
    )

    st.bar_chart(priority_counts)

    # --------------------------------------------------
    # TOP REORDER POINTS
    # --------------------------------------------------

    st.header("🔄 Products with Highest Reorder Points")

    top_reorder = (
        inventory
        .sort_values(
            "ReorderPoint",
            ascending=False
        )
        .head(15)
    )

    st.dataframe(
        top_reorder[
            [
                "StockCode",
                "Description",
                "AverageDailyDemand",
                "DemandStd",
                "SafetyStock",
                "ReorderPoint",
                "InventoryPriority"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # SAFETY STOCK
    # --------------------------------------------------

    st.header("🛡️ Safety Stock Analysis")

    top_safety_stock = (
        inventory
        .sort_values(
            "SafetyStock",
            ascending=False
        )
        .head(15)
    )

    st.bar_chart(
        top_safety_stock.set_index(
            "Description"
        )["SafetyStock"]
    )

    # --------------------------------------------------
    # FILTER BY PRIORITY
    # --------------------------------------------------

    st.header("🔎 Inventory Details")

    selected_priority = st.selectbox(
        "Select Inventory Priority",
        ["All", "Low", "Medium", "High"]
    )

    if selected_priority == "All":

        filtered_inventory = inventory

    else:

        filtered_inventory = inventory[
            inventory["InventoryPriority"]
            == selected_priority
        ]

    st.dataframe(
        filtered_inventory,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Inventory recommendations use historical demand with "
        "project assumptions for lead time and service level. "
        "They should be validated against actual supplier data "
        "before operational use."
    )

    # --------------------------------------------------
# PAGE 10: ORDER & TRANSACTION
# --------------------------------------------------

elif page == "Order & Transaction":

    st.title("🧾 Order & Transaction Dashboard")

    st.markdown(
        "Analyze order volume, transaction size, revenue per order, "
        "and purchasing activity."
    )

    # --------------------------------------------------
    # ORDER-LEVEL DATA
    # --------------------------------------------------

    order_data = (
        clean_data
        .groupby("InvoiceNo")
        .agg(
            CustomerID=("CustomerID", "first"),
            OrderRevenue=("TotalRevenue", "sum"),
            Items=("Quantity", "sum"),
            Products=("StockCode", "nunique"),
            Country=("Country", "first"),
            OrderDate=("InvoiceDate", "first")
        )
        .reset_index()
    )

    # --------------------------------------------------
    # ORDER KPIs
    # --------------------------------------------------

    total_orders = len(order_data)

    average_order_revenue = (
        order_data["OrderRevenue"].mean()
    )

    average_items_per_order = (
        order_data["Items"].mean()
    )

    average_products_per_order = (
        order_data["Products"].mean()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Orders",
            f"{total_orders:,}"
        )

    with col2:
        st.metric(
            "Avg Order Revenue",
            f"£{average_order_revenue:,.2f}"
        )

    with col3:
        st.metric(
            "Avg Items / Order",
            f"{average_items_per_order:,.1f}"
        )

    with col4:
        st.metric(
            "Avg Products / Order",
            f"{average_products_per_order:,.1f}"
        )

    st.divider()

    # --------------------------------------------------
    # ORDERS OVER TIME
    # --------------------------------------------------

    
    order_data["OrderDate"] = pd.to_datetime(
    order_data["OrderDate"]
    )

    orders_by_day = (
    order_data
    .set_index("OrderDate")
    .resample("D")
    .size()
    )

    st.line_chart(orders_by_day)

    # --------------------------------------------------
    # ORDER REVENUE DISTRIBUTION
    # --------------------------------------------------

    st.header("💰 Order Revenue Distribution")

    order_revenue_bins = pd.cut(
        order_data["OrderRevenue"],
        bins=[0, 50, 100, 250, 500, 1000, 5000, float("inf")],
        labels=[
            "£0–£50",
            "£50–£100",
            "£100–£250",
            "£250–£500",
            "£500–£1,000",
            "£1,000–£5,000",
            "£5,000+"
        ]
    )

    order_revenue_distribution = (
        order_revenue_bins
        .value_counts()
        .sort_index()
    )

    st.bar_chart(order_revenue_distribution)

    # --------------------------------------------------
    # TOP ORDERS
    # --------------------------------------------------

    st.header("🏆 Highest Revenue Orders")

    top_orders = (
        order_data
        .sort_values(
            "OrderRevenue",
            ascending=False
        )
        .head(20)
    )

    st.dataframe(
        top_orders,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # ORDER SIZE
    # --------------------------------------------------

    st.header("🛒 Order Size Analysis")

    order_size = (
        order_data["Items"]
        .describe()
        .to_frame("Items per Order")
    )

    st.dataframe(
        order_size,
        use_container_width=True
    )

    # --------------------------------------------------
    # TRANSACTION FILTER
    # --------------------------------------------------

    st.header("🔎 Transaction Details")

    selected_country = st.selectbox(
        "Filter by Country",
        ["All"] +
        sorted(
            clean_data["Country"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    if selected_country == "All":

        filtered_transactions = clean_data

    else:

        filtered_transactions = clean_data[
            clean_data["Country"] == selected_country
        ]

    st.dataframe(
        filtered_transactions[
            [
                "InvoiceNo",
                "InvoiceDate",
                "CustomerID",
                "StockCode",
                "Description",
                "Quantity",
                "UnitPrice",
                "TotalRevenue",
                "Country"
            ]
        ].head(500),
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Transaction analysis is based on the cleaned dataset. "
        "Cancelled invoices and invalid quantities were removed "
        "during the data-cleaning stage."
    )

    # --------------------------------------------------
# PAGE 11: ADVANCED ANALYTICS
# --------------------------------------------------

elif page == "Advanced Analytics":

    st.title("🤖 Advanced Analytics Dashboard")

    st.markdown(
        "Explore machine learning results, customer segmentation, "
        "churn prediction, forecasting, and inventory analytics."
    )

    # --------------------------------------------------
    # MODEL FILES
    # --------------------------------------------------

    churn_evaluation = pd.read_csv(
        DATA_DIR / "churn_model_evaluation.csv"
    )

    lstm_evaluation = pd.read_csv(
        DATA_DIR / "lstm_evaluation.csv"
    )

    clustering_evaluation = pd.read_csv(
        DATA_DIR / "clustering_evaluation.csv"
    )

    # --------------------------------------------------
    # MODEL PERFORMANCE
    # --------------------------------------------------

    st.header("📊 Churn Model Performance")

    st.dataframe(
        churn_evaluation,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("ROC-AUC Comparison")

    churn_auc = (
        churn_evaluation
        .set_index("Model")["ROC_AUC"]
    )

    st.bar_chart(churn_auc)

    # --------------------------------------------------
    # CHURN RISK
    # --------------------------------------------------

    st.header("⚠️ Customer Churn Risk")

    risk_counts = (
        churn_predictions["RiskLevel"]
        .value_counts()
        .reindex(
            ["Low", "Medium", "High"]
        )
        .fillna(0)
    )

    st.bar_chart(risk_counts)

    # --------------------------------------------------
    # CUSTOMER SEGMENTATION
    # --------------------------------------------------

    st.header("👥 Customer Segmentation")

    segment_counts = (
        customer_segments["Segment"]
        .value_counts()
    )

    st.bar_chart(segment_counts)

    st.dataframe(
        customer_segments.groupby("Segment")
        .agg(
            Customers=("CustomerID", "count"),
            AvgRecency=("Recency", "mean"),
            AvgFrequency=("Frequency", "mean"),
            AvgMonetary=("Monetary", "mean")
        )
        .round(2)
        .reset_index(),
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # CLUSTERING EVALUATION
    # --------------------------------------------------

    st.header("🔬 Clustering Evaluation")

    st.dataframe(
        clustering_evaluation,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Silhouette Score")

    clustering_chart = (
        clustering_evaluation
        .set_index("Method")["Silhouette_Score"]
    )

    st.bar_chart(clustering_chart)

    # --------------------------------------------------
    # FORECAST MODEL PERFORMANCE
    # --------------------------------------------------

    st.header("📈 Forecast Model Performance")

    prophet_mape = 22.69
    lstm_mape = (
        lstm_evaluation["MAPE"].iloc[0]
    )

    forecast_performance = pd.DataFrame(
        {
            "Model": [
                "Prophet",
                "LSTM"
            ],
            "MAPE": [
                prophet_mape,
                lstm_mape
            ]
        }
    )

    st.dataframe(
        forecast_performance,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        forecast_performance.set_index(
            "Model"
        )["MAPE"]
    )

    # --------------------------------------------------
    # INVENTORY ANALYTICS
    # --------------------------------------------------

    st.header("📦 Inventory Risk Analysis")

    inventory_priority = (
        inventory["InventoryPriority"]
        .value_counts()
        .reindex(
            ["Low", "Medium", "High"]
        )
        .fillna(0)
    )

    st.bar_chart(inventory_priority)

    # --------------------------------------------------
    # SUMMARY
    # --------------------------------------------------

    st.header("📋 Analytics Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Customers Segmented",
            f"{len(customer_segments):,}"
        )

    with col2:
        st.metric(
            "High Churn Risk",
            f"{(churn_predictions['RiskLevel'] == 'High').sum():,}"
        )

    with col3:
        st.metric(
            "High Inventory Risk",
            f"{(inventory['InventoryPriority'] == 'High').sum():,}"
        )

    st.info(
        "Model metrics are based on the experiments completed "
        "during the RetailPulse analysis. Forecast MAPE and churn "
        "metrics should be interpreted together with the documented "
        "validation methodology."
    )

    # --------------------------------------------------
# PAGE 12: INTERACTIVE FILTERS
# --------------------------------------------------

elif page == "Interactive Filters":

    st.title("🎛️ Interactive Filter Dashboard")

    st.markdown(
        "Use the filters below to explore RetailPulse data "
        "interactively."
    )

    # --------------------------------------------------
    # CREATE FILTER DATASET
    # --------------------------------------------------

    interactive_data = clean_data.copy()

    interactive_data = interactive_data.merge(
        customer_segments[
            ["CustomerID", "Segment"]
        ],
        on="CustomerID",
        how="left"
    )

    interactive_data = interactive_data.merge(
        churn_predictions[
            ["CustomerID", "RiskLevel", "ChurnProbability"]
        ],
        on="CustomerID",
        how="left"
    )

    # --------------------------------------------------
    # FILTERS
    # --------------------------------------------------

    st.header("🔎 Filters")

    col1, col2 = st.columns(2)

    with col1:

        country_options = sorted(
            interactive_data["Country"]
            .dropna()
            .unique()
            .tolist()
        )

        selected_countries = st.multiselect(
            "Country",
            country_options,
            default=country_options
        )

    with col2:

        segment_options = sorted(
            interactive_data["Segment"]
            .dropna()
            .unique()
            .tolist()
        )

        selected_segments = st.multiselect(
            "Customer Segment",
            segment_options,
            default=segment_options
        )

    col3, col4 = st.columns(2)

    with col3:

        risk_options = [
            "Low",
            "Medium",
            "High"
        ]

        selected_risks = st.multiselect(
            "Churn Risk",
            risk_options,
            default=risk_options
        )

    with col4:

        inventory_options = [
            "Low",
            "Medium",
            "High"
        ]

        selected_inventory_priority = st.multiselect(
            "Inventory Priority",
            inventory_options,
            default=inventory_options
        )

    # --------------------------------------------------
    # APPLY FILTERS
    # --------------------------------------------------

    filtered_data = interactive_data[
        interactive_data["Country"].isin(
            selected_countries
        )
        &
        interactive_data["Segment"].isin(
            selected_segments
        )
        &
        interactive_data["RiskLevel"].isin(
            selected_risks
        )
    ]

    # --------------------------------------------------
    # KPIs
    # --------------------------------------------------

    st.divider()

    total_revenue = filtered_data[
        "TotalRevenue"
    ].sum()

    total_transactions = len(
        filtered_data
    )

    total_customers = filtered_data[
        "CustomerID"
    ].nunique()

    average_transaction = (
        filtered_data["TotalRevenue"].mean()
        if len(filtered_data) > 0
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Filtered Revenue",
            f"£{total_revenue:,.0f}"
        )

    with col2:
        st.metric(
            "Transactions",
            f"{total_transactions:,}"
        )

    with col3:
        st.metric(
            "Customers",
            f"{total_customers:,}"
        )

    with col4:
        st.metric(
            "Avg Transaction",
            f"£{average_transaction:,.2f}"
        )

    # --------------------------------------------------
    # FILTERED REVENUE TREND
    # --------------------------------------------------

    st.header("📈 Filtered Revenue Trend")

    if len(filtered_data) > 0:

        filtered_daily_revenue = (
            filtered_data
            .groupby("InvoiceDate")["TotalRevenue"]
            .sum()
        )

        st.line_chart(
            filtered_daily_revenue
        )

    else:

        st.warning(
            "No transactions match the selected filters."
        )

    # --------------------------------------------------
    # FILTERED COUNTRY REVENUE
    # --------------------------------------------------

    st.header("🌍 Revenue by Country")

    if len(filtered_data) > 0:

        filtered_country_revenue = (
            filtered_data
            .groupby("Country")["TotalRevenue"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(15)
        )

        st.bar_chart(
            filtered_country_revenue
        )

    # --------------------------------------------------
    # FILTERED CUSTOMER RISK
    # --------------------------------------------------

    st.header("⚠️ Churn Risk")

    filtered_risk = (
        filtered_data["RiskLevel"]
        .value_counts()
        .reindex(
            ["Low", "Medium", "High"]
        )
        .fillna(0)
    )

    st.bar_chart(filtered_risk)

    # --------------------------------------------------
    # FILTERED TRANSACTIONS
    # --------------------------------------------------

    st.header("🧾 Filtered Transactions")

    st.dataframe(
        filtered_data[
            [
                "InvoiceNo",
                "InvoiceDate",
                "CustomerID",
                "StockCode",
                "Description",
                "Quantity",
                "UnitPrice",
                "TotalRevenue",
                "Country",
                "Segment",
                "RiskLevel",
                "ChurnProbability"
            ]
        ].head(500),
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Showing a maximum of 500 filtered transactions."
    )