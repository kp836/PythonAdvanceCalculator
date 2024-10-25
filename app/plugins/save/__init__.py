import os
import pandas as pd
from datetime import datetime
from app.commands import Command

class SaveHistory(Command):
    command_name = "save"
    
    def __init__(self, csv_path):
        self.csv_path = os.path.abspath(csv_path)
        # Ensure the file and necessary columns exist at initialization
        if not os.path.exists(self.csv_path):
            self._initialize_csv()

    def _initialize_csv(self):
        """Create a CSV file with the necessary columns if it doesn't exist."""
        df = pd.DataFrame(columns=["Operation", "Operands", "Result", "Timestamp"])
        df.to_csv(self.csv_path, index=False)

    def execute(self, operation, operands, result):
        """Save an operation to the history."""
        # Prepare the new record
        new_record = pd.DataFrame([{
            "Operation": operation,
            "Operands": operands,
            "Result": result,
            "Timestamp": datetime.now()
        }])

        # Append directly to the file without loading the entire CSV
        new_record.to_csv(self.csv_path, mode='a', header=False, index=False)
        print(f"Operation '{operation}' saved to history.")

