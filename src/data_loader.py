import pandas as pd
import os

class DataLoader:
    def __init__(self, raw_data_dir='data/raw'):
        self.raw_dir = raw_data_dir

    def load_csv(self, filename):
        """
        Loads a CSV file from the raw data directory.
        Arguments:
            filename (str): Name of the file (e.g., 'supermarket_sales.csv')
        Returns:
            pd.DataFrame: Loaded data
        """
        path = os.path.join(self.raw_dir, filename)
        
        if not os.path.exists(path):
            raise FileNotFoundError(f"CRITICAL: File '{filename}' not found in {self.raw_dir}")
        
        print(f"   [Data] Successfully loaded {filename}")
        return pd.read_csv(path)