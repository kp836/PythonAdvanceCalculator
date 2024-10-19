import logging
from app.commands import Command


class GreetCommand(Command):
    command_name = "greet"
    
    def execute(self):
        logging.info("Hello, World!")
        print("Hello, World!")