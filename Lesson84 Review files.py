'''Reviewing files
We also looked at the basics of reading and writing files in Python, which is very handy if you want to store data. It is especially useful if you are using OOP code and have large numbers of objects to create.

This time, all of the employee data is stored in a file, so the objects will be created from that.

CREATE
First, on line 25, create an empty list called employee_list that we will store the objects in.
On line 28, open the file employees.txt in read mode, and store it as data_file.
Below that, use the readlines() function to get a list of the lines in the file and store as employees.
Inside the loop, replace the ???s on line 33 with string functions to strip the new line characters and split the line on commas ,
Replace the ??? on line 34 to create the object by unpacking the employee_data list
Finally, inside the __init__ method, replace the ??? to append the object to the employee_list when it is created.
Click RUN to see the name and hourly rate of the first employee and check that the code works!'''


class Employee:
    def __init__(self, name, category, hourly_rate, sick_days, leave_days):
        self.name = name
        self.category = category
        self.hourly_rate = hourly_rate
        self.sick_days = sick_days
        self.leave_days = leave_days
        employee_list.append(self)

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


# Create list to store employee objects
employee_list = []

# Open file with employee data
data_file = open("employees.txt", "r")
employees = data_file.readlines()

# Loop through each line, and split values into list to create employee from
for employee in employees:
    employee_data = employee.strip().split(",")
    Employee(*employee_data)

# Print the first employee's name to check it worked.
print(employee_list[0].name, employee_list[0].hourly_rate)
