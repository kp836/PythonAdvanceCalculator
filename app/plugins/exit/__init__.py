import sys
import logging
from app.commands import Command


class ExitCommand(Command):
    command_name = "exit"
    
    def execute(self):

        logging.info("Exiting...")
        sys.exit("Exiting...")