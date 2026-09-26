\# RetailPulse – AI-Powered Customer Analytics \& Demand Forecasting Platform



\## Project Overview



RetailPulse is an AI-powered customer analytics and demand forecasting platform developed as part of the Zidio Development Data Science \& Analytics internship.



The project analyzes retail transaction data to provide insights into:



\- Customer segmentation

\- Customer churn prediction

\- Demand and revenue forecasting

\- Inventory optimization

\- Business decision support



\## Dataset



The project uses the UCI Online Retail dataset containing retail transaction records.



After data cleaning:



\- Transactions: 392,692

\- Customers: 4,338

\- Products: 3,665



\## Technologies Used



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- Prophet

\- TensorFlow / LSTM

\- Streamlit

\- Matplotlib

\- Seaborn

\- Joblib

\- Jupyter Notebook



\## Project Features



\### 1. Data Cleaning and EDA

Performed data quality analysis, duplicate removal, missing-value handling, cancellation filtering, and revenue analysis.



\### 2. Customer Segmentation

Used RFM analysis and clustering techniques including K-Means and DBSCAN to identify customer groups.



\### 3. Demand Forecasting

Implemented Prophet and LSTM-based forecasting experiments using historical daily revenue data.



\### 4. Churn Prediction

Developed a Gradient Boosting model to estimate customer churn risk.



\### 5. Inventory Optimization

Calculated demand statistics, safety stock, and reorder points to identify products requiring inventory attention.



\### 6. Interactive Dashboard

Built a Streamlit dashboard displaying customer, revenue, churn, and inventory insights.



\## Project Structure



```text

retailpulse/

├── data/

│   ├── raw/

│   └── processed/

├── notebooks/

│   └── 01\_EDA.ipynb

├── src/

├── models/

├── dashboard/

│   └── app.py

├── reports/

├── requirements.txt

├── requirements\_backup.txt

└── README.md

