import pandas as pd
import logging
import inspect
from abc import ABC, abstractmethod
from datetime import datetime
import os


class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    history = {
        'Operation': [],
        'Operands': [],
        'Result': [],
        'Timestamp': []
    }

    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, input_command: str):
        parts = input_command.split()
        
        if not parts:
            return

        command_name = parts[0]
        args = parts[1:]
        
        try:
            # Execute the command and get the output
            result = self.commands[command_name].execute(*args)
            print(f"Result: {result}")
            # Record the command details in history with timestamp
            self.record_history(command_name, args, result)
        except KeyError:
            logging.error(f"No such command: {command_name}")
            print(f"No such command: {command_name}")
        except TypeError as e:
            logging.error(f"Invalid arguments for command '{command_name}': {e}")
            print(f"Invalid arguments for command: {command_name}")
        except Exception as e:
            logging.error(f"Error executing command '{command_name}': {e}")
            print(f"Error executing command: {command_name}")
    
    def add_command(self, command_name: str, command: Command):
        self.command[command_name] = command

    def record_and_save(self, operation_name: str, operands: list, result):
        """Record operation and save to history."""
        self.record_history(operation_name, operands, result)
        if self.save_history_command:
            self.save_history_command.execute(operation_name, operands, result)

    def record_history(self, command_name: str, operands: list, result):
        self.history['Operation'].append(command_name)
        self.history['Operands'].append(operands)
        self.history['Result'].append(result)
        timestamp = datetime.now().isoformat()
        self.history['Timestamp'].append(timestamp)
        logging.info(f"Recorded operation '{command_name}' with operands {operands} and result {result}")
    
    def save_history(self, operation_name: str, operands: list, result):
        if self.save_history_command:
            self.save_history_command.execute(operation_name, operands, result)
        
    
    def clear_history(self):
        self.history = {
            'Operation': [],
            'Operands': [],
            'Result': [],
            'Timestamp': []
        }
        logging.info("Command history cleared.")
    
    def remove_history(self, idx: list):
        current_len = len(self.history['Operation'])
        if any(i >= current_len for i in idx):
            raise IndexError("Index out of range. Please specify valid indices.")
        
        for key in self.history.keys():
            self.history[key] = [self.history[key][i] for i in range(current_len) if i not in idx]
        
    def convert_history(self) -> pd.DataFrame:
        return pd.DataFrame(self.history)
    def save_to_history(self, command_name:str, input: list):
        try:
            output = self.commands[command_name].execute(*input)
            self.record_history(command_name, input, output)
        except KeyError as e:
            frm = inspect.trace()[-1]
            msg = f"KeyError: '{command_name}' command is not available"
            logging.error(e, exe_info=True)
            print(msg)
        except Exception as e:
            logging.error(e, exc_info=True)
            print(f'Exception: {e}')
            

