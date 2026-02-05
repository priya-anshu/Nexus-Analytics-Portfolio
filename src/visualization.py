"""
Module: visualization.py
Description: Production-quality plotting for Retail Analytics.
"""
import matplotlib.pyplot as plt
import seaborn as sns
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

    def plot_hourly_sales_by_day(self, df):
        """Heatmap showing busiest hours of the week."""
        pivot = df.pivot_table(index='Day_Name', columns='Hour', values='Total', aggfunc='sum')
        # Sort days correctly
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pivot = pivot.reindex(days)
        
        plt.figure(figsize=(14, 7))
        sns.heatmap(pivot, cmap='coolwarm', annot=True, fmt=".0f", linewidths=.5)
        plt.title('Store Traffic Heatmap: Sales ($) by Day & Hour', fontweight='bold')
        self._save('01_traffic_heatmap.png')

    def plot_category_performance(self, df):
        """Bar chart of Product Line performance with Gender breakdown."""
        plt.figure()
        # Order by total sales
        order = df.groupby('Product_Line')['Total'].sum().sort_values(ascending=False).index
        
        sns.barplot(data=df, x='Total', y='Product_Line', hue='Gender', estimator=sum, order=order, ci=None)
        plt.title('Revenue by Product Line & Gender', fontweight='bold')
        plt.xlabel('Total Revenue ($)')
        self._save('02_category_performance.png')

    def plot_forecast_results(self, historical_data, y_test, predictions):
        """Line chart comparing Actual vs Predicted sales."""
        plt.figure()
        
        # Plot last 60 days of history
        recent_history = historical_data.iloc[-60:]
        plt.plot(recent_history['Date'], recent_history['Total'], label='Historical Sales', color='gray', alpha=0.5)
        
        # Plot Actual Test Data
        test_dates = historical_data.iloc[-15:]['Date']
        plt.plot(test_dates, y_test, label='Actual Sales (Test)', color='blue', linewidth=2)
        
        # Plot Predictions
        plt.plot(test_dates, predictions, label='AI Forecast', color='red', linestyle='--', linewidth=2)
        
        plt.title('Sales Forecast Model: AI vs Reality (Last 15 Days)', fontweight='bold')
        plt.legend()
        self._save('03_sales_forecast.png')