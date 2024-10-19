import sys
import logging
from app.commands import Command


class MultiplyCommand(Command):
    command_name = "multiply"
    
    def execute(self, *args):
        if len(args) != 2:
            logging.warning("Incorrect number of arguments provided.")
            print("Usage: multiply n n (Example: multiply 3 6)")
            return
        
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = num1 * num2
            logging.info(f"Multiplication successful: {num1} + {num2} = {result}")
            print(f"Result: {num1 * num2}")
        except ValueError:
            logging.error("Multiplication unsuccessful! Non-numeric values provided.")
            print("Please provide two valid numbers.")