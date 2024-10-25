### Advanced Python Calculator
This is a Advanced Calculator made in Python for command-line integration with plugins for a robust calculations and maintaining a history using pandas library. 
## To install the project:
1. git clone git@github.com:kp836/PythonAdvanceCalculator.git
2. Install the dependencies using: pip install -r requirements.txt
3. Run the calculator using: python3 main.py
4. User will be guided through 

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
- Error messages are displayed to the users and logged so that they can be fixed.  
4. Incomplete calculation history 
*** Available in plugins but unable to populate the csv file ***
## Design Patterns 
- Facade Pattern is used to Offer a simplified interface for complex pandas data manipulations.  
__The function of main.py is to start the App from the command-line and that class will handle all the functionality while the main.py is kept clean of code and functionality.__  
- Command Pattern is used to structure commands within the REPL for effective calculation. 
__All the commands are in one particular folder controlled by the same class making them unified and performing the tasks in a similar manner and not having to repeat the code multiple times.__  
- Easier to Ask for Forgiveness then Permission (EAFP) is used to check for conditions and providing necessary logging and printing outputs.  
- There are multiple examples of EAFP pattern which is to have try...except code rather than if...else conditions. One example is app/plugins/divide/__init__.py Lines 15-27. The second example is app/plugins/add/__init__.py Lines 15-24. 
## Version Control
- Git is used for Version Control purposes. Several branches with logical names that go with each feature. Commit history shows the program going from one version to next with full documentation provided by Github.
## Coverage
- 100% Coverage done using pytest, pylint, and coverage.
## Github Actions
- Used Github Actions and passed all tests
## Video Link
- Here [https://youtu.be/Bc7WegGGmuU]