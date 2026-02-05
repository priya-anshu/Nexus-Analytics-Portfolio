import pandas as pd
import numpy as np
import os

class DataLoader:
    def __init__(self, raw_data_dir='data/raw'):
        self.raw_dir = raw_data_dir
        os.makedirs(self.raw_dir, exist_ok=True)

    def load_csv(self, filename):
        path = os.path.join(self.raw_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {filename} not found.")
        print(f"   [Data] Loaded {filename}")
        return pd.read_csv(path)

    def generate_synthetic_data(self):
        """Generates detailed datasets for Projects 2-5."""
        print("   [Setup] Generating Rich Synthetic Data for Multi-Domain Analysis...")
        
        # 2. Education: Added Gender and Study Method
        if not os.path.exists(f"{self.raw_dir}/student_performance.csv"):
            n = 500
            df = pd.DataFrame({
                'Student_ID': range(n),
                'Study_Hours': np.random.normal(5, 2, n).clip(1, 10),
                'Attendance': np.random.randint(60, 100, n),
                'Gender': np.random.choice(['Male', 'Female'], n),
                'Method': np.random.choice(['Self-Study', 'Group', 'Online'], n)
            })
            # Score depends on hours + noise
            df['Score'] = (40 + 4 * df['Study_Hours'] + np.random.normal(0, 5, n)).clip(0, 100)
            df.to_csv(f"{self.raw_dir}/student_performance.csv", index=False)

        # 3. Healthcare: Added Deaths and Testing numbers
        if not os.path.exists(f"{self.raw_dir}/healthcare_covid.csv"):
            dates = pd.date_range('2024-01-01', periods=120)
            df = pd.DataFrame({'Date': dates})
            # Epidemic Curve
            x = np.linspace(0, np.pi, 120)
            df['New_Cases'] = (1000 + 2000 * np.sin(x) + np.random.normal(0, 50, 120)).astype(int)
            df['Recovered'] = df['New_Cases'].shift(10).fillna(0) * 0.90
            df['Deaths'] = df['New_Cases'].shift(14).fillna(0) * 0.02
            df.to_csv(f"{self.raw_dir}/healthcare_covid.csv", index=False)

        # 4. Finance: Added Volume and Sector
        if not os.path.exists(f"{self.raw_dir}/finance_stocks.csv"):
            dates = pd.date_range('2024-01-01', periods=100)
            df = pd.DataFrame({'Date': dates})
            # Random Walk
            df['Close_Price'] = np.cumsum(np.random.randn(100)) + 150
            df['Volume'] = np.random.randint(1000, 5000, 100)
            df.to_csv(f"{self.raw_dir}/finance_stocks.csv", index=False)

        # 5. Weather: Added Humidity and Rainfall
        if not os.path.exists(f"{self.raw_dir}/weather_data.csv"):
            dates = pd.date_range('2024-01-01', periods=365)
            df = pd.DataFrame({'Date': dates})
            df['Temp_C'] = 20 + 15 * np.sin(np.linspace(0, 2*np.pi, 365)) + np.random.normal(0, 2, 365)
            df['Rainfall_mm'] = np.where(np.random.rand(365) > 0.8, np.random.exponential(5, 365), 0)
            df['Humidity'] = 50 + 20 * np.sin(np.linspace(0, 2*np.pi, 365)) + np.random.normal(0, 5, 365)
            df.to_csv(f"{self.raw_dir}/weather_data.csv", index=False)