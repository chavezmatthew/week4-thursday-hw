# 1. Encapsulation in Personal Budget Management

# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters. Students will apply these concepts to create a Personal Budget Management system.

# Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.


# Task 1: Define Budget Category Class - Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

# Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

class BudgetCategory():
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__original_budget = allocated_budget
        self.__expenses = 0

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

    def get_info(self):
        print(f"Category: {self.get_category_name()}, Budget: {self.get_allocated_budget()}")

    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget (self):
        return self.__allocated_budget
    
    def get_original_budget(self):
        return self.__original_budget
    
    def get_expenses(self):
        return self.__expenses

    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name
        print(f"Category has been set to: {new_category_name}")

    def set_allocated_budget (self, new_budget):
        if new_budget > 0:
            self.__allocated_budget = new_budget
            self.__original_budget = new_budget
            self.__expenses = 0
            print(f"Budget has been set to: {new_budget}")
        else:
            print("Please enter a positive number.")

# Task 3: Add Budget Functionality - Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.

    def add_expenses(self, expense):
        if expense > self.__allocated_budget:
            print(f"Sorry that is too expensive for your budget of {self.__allocated_budget}")
        else:
            self.__allocated_budget -= expense
            self.__expenses += expense
            print (f"Expense of {expense} was deducted from your budget. Your new budget is {self.__allocated_budget}")


# Task 4: Display Budget Details - Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

    def display_category_summary (self):
        print(f'''
Category Summary:

Category: {self.get_category_name()}
Original budget: {self.get_original_budget()}
Expenses: {self.get_expenses()}
Updated budget: {self.get_allocated_budget()}
''')


# Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

vehicle = BudgetCategory("Car", 1500)

vehicle.get_category_name()
vehicle.get_allocated_budget()
vehicle.get_info()
vehicle.set_category_name("Boat")
vehicle.set_allocated_budget(5000)
vehicle.get_info()
vehicle.set_allocated_budget(-9000)
vehicle.get_info()

# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

vehicle.add_expenses(3000)
vehicle.get_info()
vehicle.add_expenses(3000)
vehicle.get_info()


# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.


vehicle.display_category_summary()



