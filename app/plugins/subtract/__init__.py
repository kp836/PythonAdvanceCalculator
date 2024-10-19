import sys
import logging
from app.commands import Command


class SubtractCommand(Command):
    command_name = "subtract"
    
    def execute(self, *args):
        if len(args) != 2:
            logging.warning("Incorrect number of arguments provided.")
            print("Usage: subtract n n (Example: subtract 10 3)")
            return
        
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = num1 - num2
            logging.info(f"Subtraction successful: {num1} - {num2} = {result}")
            print(f"Result: {num1 - num2}")
        except ValueError:
            logging.error("Invalid input: Non-numeric values provided.")
            print("Please provide two valid numbers.")
        