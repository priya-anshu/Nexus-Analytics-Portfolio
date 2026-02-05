"""
Nexus Analytics Portfolio - Retail Deep Dive
Author: User
Description: Advanced Retail Analytics pipeline with Machine Learning forecasting.
"""
from src.data_loader import DataLoader
from src.features import engineer_features
from src.statistics import StatEngine
from src.forecasting import train_sales_forecast_model
from src.visualization import Visualizer

def main():
    print("🚀 INITIALIZING DEEP-DIVE RETAIL ANALYTICS...\n")
    
    # 1. Setup
    loader = DataLoader()
    viz = Visualizer()
    stats = StatEngine() # Uses the existing statistics.py
    
    # 2. Ingest Data
    try:
        df_raw = loader.load_csv('supermarket_sales.csv')
    except Exception as e:
        print(f"❌ Error: {e}")
        return

    # 3. Feature Engineering (The Advanced Part)
    df = engineer_features(df_raw)

    # 4. Statistical Analysis
    print("\n--- 📊 PHASE 1: STATISTICAL VALIDATION ---")
    
    # Insight 1: Do Members spend significantly more than Normal customers?
    mem_spend = df[df['Customer_Type'] == 'Member']['Total']
    norm_spend = df[df['Customer_Type'] == 'Normal']['Total']
    print(stats.run_ttest_ind(mem_spend, norm_spend, "Member", "Normal"))
    
    # Insight 2: Does the "Branch" location affect Customer Ratings? (ANOVA)
    print("\n[Analysis] Testing Branch Consistency (ANOVA on Ratings)...")
    branch_groups = {
        'A': df[df['Branch'] == 'A']['Rating'],
        'B': df[df['Branch'] == 'B']['Rating'],
        'C': df[df['Branch'] == 'C']['Rating']
    }
    print(stats.run_anova(branch_groups))

    # 5. Visual Analysis
    print("\n--- 🎨 PHASE 2: VISUAL INSIGHTS ---")
    viz.plot_hourly_sales_by_day(df)
    viz.plot_category_performance(df)

    # 6. Machine Learning Forecasting
    print("\n--- 🤖 PHASE 3: AI SALES FORECASTING ---")
    model_data, predictions, y_test = train_sales_forecast_model(df)
    viz.plot_forecast_results(model_data, y_test, predictions)

    print("\n✅ PROJECT COMPLETE. High-Resolution reports saved in 'reports/figures/'.")

if __name__ == "__main__":
    main()