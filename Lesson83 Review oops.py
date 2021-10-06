'''''Review OOP basics
Let's review the key concepts of OOP that we learned about.

A class is a collection of attributes and methods. These attributes and methods are generally related to each other. For example, a Student class might have attributes for all of the student's personal details, and methods for updating these details, and managing results for assignments and tests.

We can create instances of a class, which we call objects, and this lets us store data within the object instead of having hundreds of different variables.

CREATE
In the editor is an employee class which might be for a program that manages pay for a company.

In the __init__ method, replace the ???s to set the remaining attributes.
Outside of the class, one employee object called jack has been created. Create kate using the details below.
Jack's name has been printed on line 28. Below it, print kate's category.
Under the relevant print statement, call the calculate_pay() method on kate who has worked 40 hours this week, and print the returned value.
Finally, jack has taken 2 days sick leave, so call the correct function under the relevant print statement and print out his remaining sick days.
'''


class Employee:
    def __init__(self, name, category, hourly_rate, sick_days, leave_days):
        self.name = name
        self.category = category
        self.hourly_rate = hourly_rate
        self.sick_days = sick_days
        self.leave_days = leave_days

    def calculate_pay(self, hours_worked):
        gross_pay = hours_worked * self.hourly_rate
        return gross_pay

    def do_sick_leave(self, days):
        if days > 0 and days < self.sick_days:
            self.sick_days -= days
            return self.sick_days

    def do_annual_leave(self, days):
        if days > 0 and days < self.leave_days:
            self.leave_days -= days
            return self.leave_days


# Create some employees
jack = Employee("Jack Williams", "editor", 15.50, 5, 20)
kate = Employee("Kate Boon", "manager", 35, 5, 20)

# Print some attributes
print(jack.name)
print(kate.category)

# Calculate Kate's weekly pay for 40 hours and print
print("Kate's weekly pay before tax:")
print(kate.calculate_pay(40))

# Take off 2 days sick leave from Jack and print remaining days
print("Jack's remaining sick days: ")
print(jack.do_sick_leave(2))
