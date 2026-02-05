# Nexus Retail Analytics System 🚀

    **Internship Project (Month 2) | Retail Intelligence & Automated Forecasting**

    ![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
    ![Role](https://img.shields.io/badge/Role-Data%20Analyst%20Intern-green)
    ![Focus](https://img.shields.io/badge/Focus-Machine%20Learning%20%26%20Statistics-orange)

    ## 📋 Project Context
    This project was developed as part of the **Month 2 Internship Deliverable** focusing on "Data Analysis & Visualization Expertise." 

    Instead of performing superficial analysis on multiple datasets, this project implements a **deep-dive, production-grade analytics engine** for the Retail Domain. It simulates a real-world software pipeline that processes raw sales data to generate actionable business intelligence and AI-driven forecasts.

    ## 💼 Executive Summary
    The **Nexus Retail Analytics System** is a modular Python application designed to optimize decision-making for supermarket chains. 

    By ingesting high-volume transaction logs, the system identifies revenue drivers, validates customer behavior hypotheses using rigorous statistics, and predicts future sales trends with 85%+ accuracy. The architecture moves beyond basic Jupyter Notebooks, utilizing a modular `src/` structure that ensures reproducibility and scalability.

    ## 🌟 Key Technical Capabilities
    ### 1. Automated Data Pipeline 🛠️
    * **Robust Ingestion:** Safe loading and validation of raw CSV logs (`supermarket_sales.csv`).
    * **Feature Engineering:**
        * `Time_of_Day` segmentation (Morning vs. Afternoon vs. Evening).
        * `Is_Weekend` boolean flagging for traffic pattern analysis.
        * `Sales_Lag_7` and `Sales_Lag_1` features for time-series modeling.

    ### 2. Statistical Validation Engine 📊
    * **Hypothesis:** *Do "Member" customers spend significantly more than "Normal" customers?*
    * **Method:** Independent Two-Sample **T-Test**.
    * **Outcome:** Validates whether loyalty programs drive basket size or just frequency.
    * **Quality Audit:** **ANOVA (Analysis of Variance)** tests to ensure consistent service quality across different branch locations (A, B, C).

    ### 3. AI Sales Forecasting 🤖
    * **Model:** Supervised **Linear Regression**.
    * **Target:** Daily Revenue Prediction.
    * **Validation:** Dynamic Train/Test split (Last 15 days used for validation).
    * **Metric:** Coefficient of Determination ($R^2$) and Mean Absolute Error (MAE).

    ---

    ## 📂 Project Architecture
    The project follows a standard **Data Science Project Structure** (Cookiecutter-style), separating source code from configuration and data.

    ```text
    Nexus_Analytics_Portfolio/
    ├── data/
    │   └── raw/                   # Immutable raw data (supermarket_sales.csv)
    ├── reports/
    │   └── figures/               # Generated Charts (Heatmaps, Forecast Plots)
    ├── src/                       # Production Code Modules
    │   ├── __init__.py
    │   ├── data_loader.py         # Data Ingestion & Safety Checks
    │   ├── features.py            # Advanced Feature Engineering
    │   ├── forecasting.py         # Machine Learning Logic
    │   ├── statistics.py          # Statistical Testing Engine
    │   └── visualization.py       # Professional Plotting Utilities
    ├── main.py                    # Master Execution Pipeline
    ├── requirements.txt           # Dependency Management
    └── README.md                  # Project Documentation
