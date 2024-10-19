import sys
import logging
from app.commands import Command

class VarianceCommand(Command):
    command_name = "variance"

    def execute(self, *args):
        if len(args) < 2:
            logging.warning("Insufficient values provided for variance calculation.")
            print("Usage: variance n n ... (Example: variance 5 7 2)")
            return
        
        try: 
            numbers = [float(num) for num in args]
            MeanValue = sum(numbers) / len(numbers)
            variance = sum((x - MeanValue) ** 2 for x in numbers) / len(numbers)
            logging.info(f"Variance calculation successful: {numbers} -> Variance = {variance}")
            print(f"{numbers} -> Variance = {variance}")
        except ValueError:
            logging.error("Variance calculation unsuccessful! Non-numeric values provided.")
            print("Please provide valid numbers.")
            

