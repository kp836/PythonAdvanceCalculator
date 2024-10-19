import sys
import logging
from app.commands import Command


class MenuCommand(Command):
    command_name = "menu"

    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        # Log when the menu command is executed
        logging.info("Menu command executed.")

        print("Available commands:")
        if not self.command_handler.commands:
            logging.warning("No available commands found.")
        else:
            for command_name in self.command_handler.commands.keys():
                # Log each command name
                logging.debug(f"Command available: {command_name}")
                print(f" - {command_name}")