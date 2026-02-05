"""
Module: forecasting.py
Description: Machine Learning models to predict future sales trends.
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def train_sales_forecast_model(df):
    """
    Trains a Linear Regression model to predict Daily Sales.
    
    Methodology:
    1. Aggregate data to Daily level.
    2. Create lag features (Sales yesterday, Sales 7 days ago).
    3. Train model to predict 'Tomorrow's Sales'.
    """
    print("\n   [ML] Initializing Sales Forecasting Engine...")
    
    # 1. Aggregate to Daily Sales
    daily_sales = df.groupby('Date')['Total'].sum().reset_index()
    daily_sales = daily_sales.sort_values('Date')
    
    # 2. Feature Engineering for ML
    # Convert Date to ordinal (number of days) for trend line
    daily_sales['Day_Index'] = np.arange(len(daily_sales))
    
    # Create 'Lag' features (Autoregression)
    # "Sales_Lag_1" means Sales Yesterday
    daily_sales['Sales_Lag_1'] = daily_sales['Total'].shift(1)
    # "Sales_Lag_7" means Sales Last Week (same day)
    daily_sales['Sales_Lag_7'] = daily_sales['Total'].shift(7)
    
    # Drop NaN values created by shifting
    model_data = daily_sales.dropna()
    
    # 3. Define X (Features) and y (Target)
    features = ['Day_Index', 'Sales_Lag_1', 'Sales_Lag_7']
    X = model_data[features]
    y = model_data['Total']
    
    # 4. Split Train/Test (Last 15 days for testing)
    X_train, X_test = X.iloc[:-15], X.iloc[-15:]
    y_train, y_test = y.iloc[:-15], y.iloc[-15:]
    
    # 5. Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 6. Evaluate
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"   [ML] Model Trained Successfully.")
    print(f"   [ML] Accuracy Report (R2 Score): {r2:.2f} (Higher is better)")
    print(f"   [ML] Mean Error: ${mae:.2f} per day")
    
    return model_data, predictions, y_test