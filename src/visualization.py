"""
Module: visualization.py
Description: Production-quality plotting for Retail Analytics.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Global Styling
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 11

class Visualizer:
    def __init__(self, output_dir='reports/figures'):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _save(self, filename):
        path = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(path, dpi=300)
        plt.close()
        print(f"   [Viz] Saved: {filename}")

    def plot_heatmap(self, df):
        """Generates heatmap for retail analysis."""
        # Check if we have the right columns
        if 'Day_Name' not in df.columns or 'Hour' not in df.columns:
            print("   [Viz Warning] Missing columns for Heatmap. Skipping.")
            return

        # Pivot the data
        sales_pivot = df.pivot_table(index='Day_Name', columns='Hour', values='Total', aggfunc='sum')
        
        # Sort days correctly
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        sales_pivot = sales_pivot.reindex(days)
        
        plt.figure(figsize=(12, 6))
        sns.heatmap(sales_pivot, cmap='YlGnBu', annot=False)
        plt.title('Retail Heatmap: Peak Business Hours', fontweight='bold')
        plt.ylabel('Day of Week')
        plt.xlabel('Hour of Day')
        self._save("01_retail_heatmap.png")

    def plot_forecast(self, historical_data, y_test, predictions):
        """Line chart comparing Actual vs Predicted sales."""
        plt.figure()
        
        # Plot Actual Test Data
        # We need to ensure indices align for plotting
        test_dates = historical_data.iloc[-len(y_test):]['Date']
        
        plt.plot(test_dates, y_test, label='Actual Sales', color='blue', linewidth=2)
        plt.plot(test_dates, predictions, label='AI Forecast', color='red', linestyle='--', linewidth=2)
        
        plt.title('Sales Forecast Model: AI vs Reality (Last 15 Days)', fontweight='bold')
        plt.legend()
        plt.xticks(rotation=45)
        self._save('01_retail_forecast.png')