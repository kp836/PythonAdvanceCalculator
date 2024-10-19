import sys
import logging
from app.commands import Command

# Class that will take two values to add as parameters
class AddCommand(Command):
    command_name = "add"

    def execute(self, *args):
        if len(args) != 2:
            logging.warning("Incorrect number of arguments provided.")
            print("Usage: add n n (Example: add 9 2)")
            return
    
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = num1 + num2
            logging.info(f"Addition successful: {num1} + {num2} = {result}")
            print(f"Result: {num1 + num2}")
        except ValueError:
            logging.error("Invalid input: Error calculating with information provided.")
            print("Please provide two positive numbers.")