### Scientific Computing with Python Projects

It's time to put your Python skills to the test. By completing these projects, you'll demonstrate that you have a strong foundational knowledge of Python. And you'll qualify for freeCodeCamp's Scientific Computing with Python Certification.


1. **Arithmetic Formatter**

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-arithmetic-formatter-3)


2. **Time Calculator**

Write a function named add_time that takes in two required parameters and one optional parameter:

- A start time in the 12-hour clock format (ending in AM or PM)
- A duration time that indicates the number of hours and minutes
- A starting day of the week, case insensitive (optional) 

The function should add the duration time to the start time and return the result.


[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-time-calculator-2#time_calculator.py)


3. **Budget App**

Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

- A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
- A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
- A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
- A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
- A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.


[See full instructions here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)


See the full solution on replit [Here](https://replit.com/@WsNdungu/boilerplate-budget-app#budget.py)