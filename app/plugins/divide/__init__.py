import sys
import logging
from app.commands import Command


class DivideCommand(Command):
    command_name = "divide"
    
    def execute(self, *args):
        if len(args) != 2:
            logging.warning("Incorrect number of arguments provided.")
            print("Usage: divide n n (Example: divide 5 2)")
            return
        
        try:
            num1 = float(args[0])
            num2 = float(args[1])

            if num2 == 0:
                logging.warning("Error: Division by zero is not allowed.")
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            logging.info(f"Division successful: {num1} + {num2} = {result}")
            print(f"Result: {num1 / num2}")
        except ValueError:
            logging.warning("Invalid input: Non-numeric values provided.")
            print("Please provide two valid numbers.")