import sys
import logging
from app.commands import Command

class AverageCommand(Command):
    command_name = "average"

    def execute(self, *args):
        if len(args) < 1:
            logging.warning("No values provided for average calculation.")
            print("Usage: average n n ... (Example: average 6 4 8)")
            return
        
        try:
            numbers = [float(num) for num in args]
            result = sum(numbers) / len(numbers)
            logging.info(f"Average calculation successful: {numbers} -> Average = {result}")
            print(f"Result: {numbers} -> Average = {result}")
        
        except ValueError:
            logging.error("Average calculation unsuccessful! Non-numeric values provided.")
            print("Please provide valid numbers.")