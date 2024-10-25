import os
import pandas as pd
from app.commands import Command

class ClearHistory(Command):
    command_name = "clear"
    def __init__(self, csv_path):
        self.csv_path = os.path.abspath(csv_path)

    def execute(self, csv_path):
        """Clear the entire history by removing all entries."""
        if os.path.exists(self.csv_path):
            # Overwrite the file with an empty DataFrame
            df = pd.DataFrame(columns=["Operation", "Operands", "Result", "Timestamp"])
            df.to_csv(self.csv_path, index=False)
            print("History cleared successfully.")
        else:
            print(f"History file not found at {self.csv_path}.")
