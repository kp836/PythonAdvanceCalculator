import os
import pandas as pd
from app.commands import Command

class DeleteHistory(Command):
    command_name = "delete"
    
    def __init__(self, csv_path):
        self.csv_path = os.path.abspath(csv_path)

    def execute(self, index):
        """Delete a specific record from the history by index."""
        if os.path.exists(self.csv_path):
            df = pd.read_csv(self.csv_path)
            if 0 <= index < len(df):
                df = df.drop(index).reset_index(drop=True)
                df.to_csv(self.csv_path, index=False)
                print(f"Deleted record at index {index}.")
            else:
                print(f"No record found at index {index}.")
        else:
            print(f"History file not found at {self.csv_path}.")
