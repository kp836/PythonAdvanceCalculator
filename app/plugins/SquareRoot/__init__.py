import sys
import logging
import math
from app.commands import Command


class SquareRootCommand(Command):
    command_name = "SquareRoot"
    
    def execute(self, *args):
        if len(args) != 1:
            logging.warning("Incorrect number of arguments provided.")
            print("Usage: sqrt n (Example: sqrt 9)")
            return
        
        try:
            num1 = float(args[0])
            if num1 < 0:
                logging.error("Square root of a negative number attempted.")
                print("Cannot take square root of a negative number.")
                return
            
            result = math.sqrt(num1)
            logging.info(f"Square root successful: sqrt({num1}) = {result}")
            print(f"Result: sqrt{num1} = {result}")
        
        except ValueError:
            logging.error("Square root unsuccessful! Non-numeric values provided.")
            print("Please provide a valid numbers.")