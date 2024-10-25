import os
import pandas as pd
from app.commands import Command

class LoadHistory(Command):
    command_name = "load"
    
    def __init__(self, csv_path):
        self.csv_path = os.path.abspath(csv_path)

    def execute(self):
        """Load and display the calculation history."""
        if os.path.exists(self.csv_path):
            df = pd.read_csv(self.csv_path)
            if df.empty:
                print("No history records available.")
            else:
                print(df)
        else:
            print(f"History file not found at {self.csv_path}.")
