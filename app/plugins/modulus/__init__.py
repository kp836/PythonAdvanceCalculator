import sys
import logging
from app.commands import Command


class ModulusCommand(Command):
    command_name = "modulus"
    
    def execute(self, *args):
        if len(args) != 2:
            logging.warning("Incorrect number of arguments provided.")
            print("Usage: modulus n n (Example: modulus 3 9)")
            return
        
        try:
            num1 = float(args[0])
            num2 = float(args[1])

            if num2 == 0:
                logging.warning("Division by zero error in modulus operation.")
                print("Cannot perform modulus by zero.")
                return
            result = num1 % num2
            logging.info(f"Modulus successful: {num1} + {num2} = {result}")
            print(f"Result: {num1 % num2}")
        except ValueError:
            logging.warning("Invalid input: Non-numeric values provided.")
            print("Please provide two valid numbers.")