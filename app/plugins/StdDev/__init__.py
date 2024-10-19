import sys
import logging
import math
from app.commands import Command

class StdDevCommand(Command):
    command_name = "stddev"

    def execute(self, *args):
        if len(args) < 2:
            logging.warning("Insufficient values provided for standard deviation calculation.")
            print("Usage: stddev n n ... (Example: stddev 7 9 1)")
            return
        
        try:
            numbers = [float(num) for num in args]
            MeanValue = sum(numbers) / len(numbers)
            variance = sum((x - MeanValue) ** 2 for x in numbers) / len(numbers)
            stddev = math.sqrt(variance)
            logging.info(f"Standard deviation calculation successful: {numbers} -> StdDev = {stddev}")
            print(f"{numbers} -> StdDev = {stddev}")
        except ValueError:
            logging.error("Standard deviation calculation unsuccessful! Non-numeric values provided.")
            print("Please provide valid numbers.")