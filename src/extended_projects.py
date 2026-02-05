"""
Module: extended_projects.py
Description: Advanced analysis for Education, Healthcare, Finance, and Weather.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

class ExtendedProjectEngine:
    def __init__(self, loader, output_dir='reports/figures'):
        self.loader = loader
        self.output_dir = output_dir
        # Standardize Plot Sizing
        plt.rcParams['figure.figsize'] = (10, 6)
        sns.set_theme(style="whitegrid")

    def _save(self, filename):
        path = os.path.join(self.output_dir, filename)
        plt.tight_layout()
        plt.savefig(path, dpi=300)
        plt.close()
        print(f"   [Viz] Generated: {filename}")

    # --- PROJECT 2: EDUCATION ---
    def run_education_deep_dive(self):
        print("\n🎓 STARTING PROJECT 2: EDUCATION ANALYTICS...")
        df = self.loader.load_csv('student_performance.csv')
        
        # Insight 1: Correlation
        corr = df[['Study_Hours', 'Attendance', 'Score']].corr().loc['Study_Hours', 'Score']
        print(f"   [Insight] Correlation (Study Hours vs Score): {corr:.2f}")

        # Viz 1: Scatter Plot with Regression
        plt.figure()
        sns.regplot(data=df, x='Study_Hours', y='Score', line_kws={"color": "red"})
        plt.title('Impact of Study Hours on Exam Performance')
        self._save('02_edu_regression.png')

        # Viz 2: Box Plot by Gender (Fixed Warning)
        plt.figure()
        sns.boxplot(data=df, x='Gender', y='Score', hue='Gender', legend=False, palette='pastel')
        plt.title('Score Distribution by Gender')
        self._save('02_edu_gender_dist.png')

        # Viz 3: Bar Chart by Method (Fixed Warning)
        plt.figure()
        sns.barplot(data=df, x='Method', y='Score', hue='Method', legend=False, errorbar=None, palette='viridis')
        plt.title('Average Score by Study Method')
        self._save('02_edu_method_perf.png')

    # --- PROJECT 3: HEALTHCARE ---
    def run_healthcare_deep_dive(self):
        print("\n🏥 STARTING PROJECT 3: HEALTHCARE EPIDEMIOLOGY...")
        df = self.loader.load_csv('healthcare_covid.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Insight: Recovery Rate
        rec_rate = (df['Recovered'].sum() / df['New_Cases'].sum()) * 100
        print(f"   [Insight] Global Recovery Rate: {rec_rate:.1f}%")

        # Viz 1: Multi-Line Epidemic Curve
        plt.figure()
        plt.plot(df['Date'], df['New_Cases'], label='Infection Rate', color='red', alpha=0.7)
        plt.plot(df['Date'], df['Recovered'], label='Recovery Rate', color='green', linestyle='--')
        plt.title('Epidemic Curve: Spread vs Recovery')
        plt.legend()
        self._save('03_health_curve.png')

        # Viz 2: Stacked Area (Cumulative)
        plt.figure()
        plt.stackplot(df['Date'], df['New_Cases'].cumsum(), df['Recovered'].cumsum(), 
                     labels=['Total Cases', 'Total Recovered'], colors=['salmon', 'lightgreen'])
        plt.title('Cumulative Caseload Analysis')
        plt.legend(loc='upper left')
        self._save('03_health_cumulative.png')

        # Viz 3: Daily Deaths Bar
        plt.figure()
        plt.bar(df['Date'], df['Deaths'], color='black', alpha=0.6)
        plt.title('Daily Mortality Trend')
        self._save('03_health_mortality.png')

    # --- PROJECT 4: FINANCE ---
    def run_finance_deep_dive(self):
        print("\n📈 STARTING PROJECT 4: FINANCIAL MARKET ANALYSIS...")
        df = self.loader.load_csv('finance_stocks.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Feature Engineering: Daily Returns & Volatility
        df['Daily_Return'] = df['Close_Price'].pct_change() * 100
        volatility = df['Daily_Return'].std()
        print(f"   [Insight] Market Volatility (Std Dev): {volatility:.2f}%")

        # Viz 1: Price Trend
        plt.figure()
        plt.plot(df['Date'], df['Close_Price'], color='navy')
        plt.title('Asset Price History (Close)')
        self._save('04_fin_price_trend.png')

        # Viz 2: Return Distribution (Risk Analysis)
        plt.figure()
        sns.histplot(df['Daily_Return'].dropna(), bins=30, kde=True, color='purple')
        plt.title('Risk Profile: Daily Return Distribution')
        self._save('04_fin_risk_dist.png')

        # Viz 3: Volume vs Price
        plt.figure()
        plt.scatter(df['Volume'], df['Daily_Return'], alpha=0.5)
        plt.title('Trading Volume vs Price Change')
        self._save('04_fin_vol_price.png')

    # --- PROJECT 5: WEATHER ---
    def run_weather_deep_dive(self):
        print("\n☁️ STARTING PROJECT 5: CLIMATE PATTERNS...")
        df = self.loader.load_csv('weather_data.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Insight: Peak Heat
        peak_temp = df['Temp_C'].max()
        print(f"   [Insight] Annual Peak Temperature: {peak_temp:.1f}°C")

        # Viz 1: Temperature Seasonality
        plt.figure()
        sns.lineplot(data=df, x='Date', y='Temp_C', color='orange')
        plt.title('Annual Temperature Cycle')
        self._save('05_weath_temp_cycle.png')

        # Viz 2: Rainfall Distribution
        plt.figure()
        plt.bar(df['Date'], df['Rainfall_mm'], color='blue', alpha=0.3)
        plt.title('Precipitation Events (Rainfall mm)')
        self._save('05_weath_rainfall.png')

        # Viz 3: Correlation Heatmap
        plt.figure()
        sns.heatmap(df[['Temp_C', 'Rainfall_mm', 'Humidity']].corr(), annot=True, cmap='coolwarm')
        plt.title('Climatic Variable Correlation')
        self._save('05_weath_correlation.png')