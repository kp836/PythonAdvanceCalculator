### Advanced Python Calculator
This is a Advanced Calculator made in Python using 
## To install the project:
1. git clone git@github.com:kp836/PythonAdvanceCalculator.git
2. Install the dependencies using: pip install -r requirements.txt
3. Run the calculator using: python3 main.py

## Features
1. Command-Line Interface (REPL - Read, Evaluate, Print, Loop) that facilitates direct interaction with the calculator. 
- Execution of operations () 
- Access to extended functionalities through dynamically loaded plugins 
2. Plugin System to allow seamless integration of new commands and features.   
    __Plugins Available__   
    __Menu__ - To show all the commands available    
    __Greet__ - To greet the user when the application starts    
    __Goodbye__ - To inform the user when the user exits   
    __Add__ - Will be used to add two values     
    __Subtract__ - Will be used to subtract two values    
    __Multiply__ - Will be used to multiply two values    
    __Divide__ - Will be used to divide and doesn't let the user divide by zero  
    __Modulus__ - Will give you the reminder left after dividing from a number and doesn't let the user divide by zero  
    __Exponent__ - Will give you the number raised to the power of whatever number provided  
    __Square Root__ - Will give you the square root of the number provided  
    __Average__ - Will give you the average of all the numbers provided (Need to be more than 2 values)  
    __Variance__ - Will give you the variance of the numbers provided (Needs to be more than 2 values)  
    __Standard Deviation__ - Will give you the standard deviation of all the numbers provided (Needs to be more than 2 values)  
    __Dynamically loads and integrates plugins without modifying the core application code.__  
    __REPL "Menu" command that lists all available plugin commands, ensuring user discoverability and interaction.__  
3. Established a comprehensive logging system to record:
- Detailed application operations, data manipulations, errors, and informational messages.  
- Different log messages by severity (INFO, WARNING, ERROR) for effective monitoring.  
- Dynamic logging configuration through environment variables for levels and output destinations.   
4. Incomplete calculation history 
*** Available in plugins but unable to populate the csv file ***
## Design Patterns 
- Facade Pattern is used to Offer a simplified interface for complex pandas data manipulations.  
- Command Pattern is used to structure commands within the REPL for effective calculation.  
- Easier to Ask for Forgiveness then Permission (EAFP) is used to check for conditions and providing necessary logging and printing outputs.  
