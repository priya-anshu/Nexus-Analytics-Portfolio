"""
Module: features.py
Description: Advanced feature engineering for Retail Analytics.
"""
import pandas as pd

def engineer_features(df):
    """
    Enhances the raw dataframe with time-based and categorical features.
    
    Args:
        df (pd.DataFrame): Raw sales data.
        
    Returns:
        pd.DataFrame: Dataframe with added 'Hour_Bin', 'Weekday', 'Is_Weekend'.
    """
    print("   [Feature Eng] Generating advanced time features...")
    
    # 1. Extract Date Components
    df['Date'] = pd.to_datetime(df['Date'])
    df['Day_Name'] = df['Date'].dt.day_name()
    df['Month_Name'] = df['Date'].dt.month_name()
    
    # 2. Weekend Flag (Critical for behavioral analysis)
    # Saturday (5) and Sunday (6) are weekends
    df['Is_Weekend'] = df['Date'].dt.dayofweek.isin([5, 6]).astype(int)
    
    # 3. Time of Day Binning
    # 06:00-12:00 = Morning, 12:00-17:00 = Afternoon, 17:00-24:00 = Evening
    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
    
    def get_time_bin(h):
        if 6 <= h < 12: return 'Morning'
        elif 12 <= h < 17: return 'Afternoon'
        else: return 'Evening'
        
    df['Time_ of_Day'] = df['Hour'].apply(get_time_bin)
    
    # 4. Revenue Calculation (if not present, though 'Total' exists)
    # Gross Margin Percentage = (Total - COGS) / Total. 
    # In this dataset, 'Tax' is 5%, implying Cost ~ Total/1.05. 
    # Let's calculate 'Gross_Income' explicitly if needed.
    
    print("   [Feature Eng] Complete. Added: Time_of_Day, Is_Weekend.")
    return df