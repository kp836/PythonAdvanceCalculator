import sys
import logging
import math
from app.commands import Command

class FactorialCommand(Command):
    command_name = "factorial"

    def execute(self, *args):
        if len(args) != 1:
            logging.warning("Incorrect number of arguments provided.")
            print("Usage: factorial n (Example: factorial 7)")
            return
        
        try:
            num1 = int(args[0])
            if num1 < 0:
                logging.error("Factorial of a negative number attempted.")
                print("Cannot take factorial of a negative number.")
                return
            
            result = math.factorial(num1)
            logging.info(f"Factorial successful: {num1}! = {result}")
            print(f"Result: {num1}! = {result}")
        except ValueError:
            logging.error("Factorial unsuccessful! Non-numeric or non-integer value provided.")
            print("Please provide a valid non-negative number.")