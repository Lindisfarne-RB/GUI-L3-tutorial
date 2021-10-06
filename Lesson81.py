'''RW Text files
all in one
Introduction to reading and writing files
One thing we have not yet managed to do in our Python code is save data. At the moment our goal tracking app only works while it is open. If we close it and run it again, the balances go back to zero.

In Python we can work with files. Doing this can improve our programs a lot. We can open a file, read it, write to it and close it, and this will allow us to both load and save data for our program:

my_file = open("my_file.txt","w")
my_file.write("Hello!")
my_file.close()

When you open a file, you can open it in different modes. Here are some common ones:

"w": write mode
"a": append mode
"r": read mode
Click here for a little more detail on file modes.
CREATE
In the editor, create a new file called details_file by opening details.txt in write mode.
Write your name into the file using .write() in the format: Name: Hannah\n.
Close the file.
Open the file again in append mode.
Write your birth date into the file in the format: Birthday: 19th April\n.
Close the file.'''

details_file = open("details.txt", "w")
details_file.write("Name: Hannah\n")
details_file.close()

details_file = open("details.txt", "a")
details_file.write("Birthday: 19th April\n")
details_file.close()
'''
Reading files
With Python files, we can read the whole file, or we can read it by lines:

my_file = open("my_file.txt", "r")
content = my_file.read()
print(content)
lines = my_file.readlines()
print(lines)

The readlines() function splits the content on \n new line characters and returns a list with each line as an item, including the newline characters. So the output of lines might look like:

['Here is line number 1\n', 'Here is line number 2\n', 'Here is line number 3']

It works just like a regular list, so we can use lines[0] to get the first item, and if we do lines[0].strip() it will remove that newline character.

CREATE
On line 9, open details.txt again in read mode this time.
Use readlines() to get the content line by line, and store as lines.
Write a for loop statement that will loop through each line in lines.
Inside the loop, print the line.
(Optional) Use .strip() in the print statement to remove the extra newline characters in the output.

'''
details_file = open("details.txt", "w")
details_file.write("Name: Hannah\n")
details_file.close()

details_file = open("details.txt", "a")
details_file.write("Birthday: 19th April\n")
details_file.close()

details_file = open("details.txt", "r")
lines = details_file.readlines()

for line in lines:
    print(line.strip())

'''
Loading our account data from a file
Reading saved data is really useful when you're using OOP.

In this task we will write a function that will load the data from accounts.txt and create the objects we need from it. We have put the data into the file for you in this format:
Savings,0,1000
Phone,0,800
Holiday,0,7000

Each account is on a new line, and all of the parameters we need to create an Account object (name, balance, goal) are separated by commas. We can split each line then into another list of values using the commas. Here's a plan for the whole function:
Open accounts file in read mode
Read lines and store as line list
Repeat for each line in line list
  Strip the data, split it on commas, store as account data
  Create an object from this account data
  
Close the file

CREATE
Since this will be the first thing that happens when the program loads, let's write it at the top of the Functions and Setup section.

On line 41, create a new function called get_data() with no parameters.
Inside the function, open accounts.txt in read mode and store as account_file.
Use readlines() to get the list of lines and store as line_list.
Write a for loop statement that will loop through each line in line_list.
Inside the loop, create a list called account_data and set it equal to the line using strip() and .split() to split on commas
TIPS

'''

####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk
import random


##################  CLASS CODE  ######################
# Create the Account class
class Account:
    """The Account class stores the details of each account and has methods to deposit, withdraw and calculate progress towards the savings goal"""

    def __init__(self, name, balance, goal):
        self.name = name
        self.balance = balance
        self.goal = goal
        account_list.append(self)

    # Deposit method adds money to balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    # Withdraw method subtracts money from balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    # Get progress method calculates goal progress
    def get_progress(self):
        progress = (self.balance / self.goal) * 100
        return progress


##############  FUNCTIONS AND SETUP ###############
# Create a function to read data from the file
def get_data():
    account_file = open("accounts.txt", "r")
    line_list = account_file.readlines()

    for line in line_list:
        account_data = line.strip().split(",")


# Create a function to get account names list
def create_name_list():
    name_list = []
    for account in account_list:
        name_list.append(account.name)
    return name_list


# Create a function that will update the balance.
def update_balance():
    total_balance = 0
    balance_string = ""

    # Append each accounts balance, progress and goal to the label
    for account in account_list:
        progress = account.get_progress()
        balance_string += "{}: ${:.2f} - {:.0f}% of ${:.2f} goal\n".format(account.name, account.balance, progress,
                                                                           account.goal)
        total_balance += account.balance

    balance_string += "\nTotal balance: ${:.2f}".format(total_balance)
    account_details.set(balance_string)


# Create the deposit function
def deposit_money(account):
    if account.deposit(amount.get()):
        message = random.choice(deposit_messages)
        message_text.set(message)
        action_feedback.set("Success! Total of ${:.2f} deposited into {}".format(amount.get(), account.name))
        image_label.configure(image=happy_image)
    else:
        action_feedback.set("Please enter a positive number")


# Create the withdraw function
def withdraw_money(account):
    if account.withdraw(amount.get()):
        message = random.choice(withdraw_messages)
        message_text.set(message)
        action_feedback.set("Success! Total of ${:.2f} withdrawn from {}".format(amount.get(), account.name))
        image_label.configure(image=sad_image)
    else:
        action_feedback.set("Not enough money in {} or not a valid amount".format(account.name))


# Create the manage action function
def manage_action():
    try:
        for account in account_list:
            if chosen_account.get() == account.name:
                if chosen_action.get() == "Deposit":
                    deposit_money(account)
                else:
                    withdraw_money(account)

        # Update the GUI
        update_balance()
        amount.set("")

    # Add an exception for text input
    except ValueError:
        action_feedback.set("Please enter a valid number")


# Set up Lists
account_list = []
deposit_messages = ["Well done, keep those deposits coming!", "You're making good progress!",
                    "Awesome! It will feel great when you reach your goal"]
withdraw_messages = ["Think about where else you might be able to save some money this week",
                     "You're doing well, but try to keep that spending under control",
                     "Tomorrow is another day for saving!"]

# Create instances of the class
savings = Account("Savings", 0, 1000)
phone = Account("Phone", 0, 800)
holiday = Account("Holiday", 0, 7000)
account_names = create_name_list()

##################  GUI CODE  ######################
root = Tk()
root.title("Goal Tracker")

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Account Details")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="/images/python/neutral.png")
happy_image = PhotoImage(file="/images/python/happy.png")
sad_image = PhotoImage(file="/images/python/sad.png")

image_label = ttk.Label(top_frame, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and set the account details variable
account_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=account_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create a label for the account combobox
account_label = ttk.Label(bottom_frame, text="Account: ")
account_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(bottom_frame, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(bottom_frame, text="Action:")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create an action feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

# Run the mainloop
update_balance()
root.mainloop()
'''Creating objects from the loaded data
Now we have a loop that is getting each line and splitting it into a list of values called account_data that looks like this (for the first line):

["Savings","0","1000"]

Before we were creating our objects manually in the code like this:

savings = Account("Savings", 0, 1000)

But we want to create each object inside this loop using the data we got from the file. We're going to use a fun little trick called unpacking so that we can create an Account object directly from the account_data list by using a  *  in front:
Account(account_data) # Won't work, wrong number args
Account(*account_data) # Will work because values unpacked

Click here for an explanation.

CREATE
Let's finish off our get_data() function.

Still inside the for loop, create an Account object by passing in the account_data list and unpacking it.
Outside the loop, close the account_file.
Now we no longer need the lines where we were creating the objects.

Scroll down and find the old code for creating the Account objects (savings, phone, holiday) and delete those 3 lines.
Replace them with a single call to get_data().'''

####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk
import random


##################  CLASS CODE  ######################
# Create the Account class
class Account:
    """The Account class stores the details of each account and has methods to deposit, withdraw and calculate progress towards the savings goal"""

    def __init__(self, name, balance, goal):
        self.name = name
        self.balance = balance
        self.goal = goal
        account_list.append(self)

    # Deposit method adds money to balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    # Withdraw method subtracts money from balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    # Get progress method calculates goal progress
    def get_progress(self):
        progress = (self.balance / self.goal) * 100
        return progress


##############  FUNCTIONS AND SETUP ###############
# Create a function to read data from the file
def get_data():
    account_file = open("accounts.txt", "r")
    line_list = account_file.readlines()

    for line in line_list:
        account_data = line.strip().split(",")
        Account(*account_data)

    account_file.close()


# Create a function to get account names list
def create_name_list():
    name_list = []
    for account in account_list:
        name_list.append(account.name)
    return name_list


# Create a function that will update the balance.
def update_balance():
    total_balance = 0
    balance_string = ""

    # Append each accounts balance, progress and goal to the label
    for account in account_list:
        progress = account.get_progress()
        balance_string += "{}: ${:.2f} - {:.0f}% of ${:.2f} goal\n".format(account.name, account.balance, progress,
                                                                           account.goal)
        total_balance += account.balance

    balance_string += "\nTotal balance: ${:.2f}".format(total_balance)
    account_details.set(balance_string)


# Create the deposit function
def deposit_money(account):
    if account.deposit(amount.get()):
        message = random.choice(deposit_messages)
        message_text.set(message)
        action_feedback.set("Success! Total of ${:.2f} deposited into {}".format(amount.get(), account.name))
        image_label.configure(image=happy_image)
    else:
        action_feedback.set("Please enter a positive number")


# Create the withdraw function
def withdraw_money(account):
    if account.withdraw(amount.get()):
        message = random.choice(withdraw_messages)
        message_text.set(message)
        action_feedback.set("Success! Total of ${:.2f} withdrawn from {}".format(amount.get(), account.name))
        image_label.configure(image=sad_image)
    else:
        action_feedback.set("Not enough money in {}  or not a valid amount".format(account.name))


# Create the manage action function
def manage_action():
    try:
        for account in account_list:
            if chosen_account.get() == account.name:
                if chosen_action.get() == "Deposit":
                    deposit_money(account)
                else:
                    withdraw_money(account)

        # Update the GUI
        update_balance()
        amount.set("")

    # Add an exception for text input
    except ValueError:
        action_feedback.set("Please enter a valid number")


# Set up Lists
account_list = []
deposit_messages = ["Well done, keep those deposits coming!", "You're making good progress!",
                    "Awesome! It will feel great when you reach your goal"]
withdraw_messages = ["Think about where else you might be able to save some money this week",
                     "You're doing well, but try to keep that spending under control",
                     "Tomorrow is another day for saving!"]

# Create instances of the class
get_data()
account_names = create_name_list()

##################  GUI CODE  ######################
root = Tk()
root.title("Goal Tracker")

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Account Details")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="/images/python/neutral.png")
happy_image = PhotoImage(file="/images/python/happy.png")
sad_image = PhotoImage(file="/images/python/sad.png")

image_label = ttk.Label(top_frame, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and set the account details variable
account_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=account_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create a label for the account combobox
account_label = ttk.Label(bottom_frame, text="Account: ")
account_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(bottom_frame, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(bottom_frame, text="Action:")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create an action feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

# Run the mainloop
update_balance()
root.mainloop()

'''Updating the file
We have one small issue to fix, and then we need to get our program to update the file whenever we deposit or withdraw money.

First, the problem. We have unpacked account_data to create the object and that works fine. However, the balance and goal values are strings now that they are coming out of the text file, and we need them to be float values.

The easiest way to fix this is to use float() in our __init__ function when the attributes are set:
def __init__(self, name, balance, goal):
    self.name = name
    self.balance = float(balance)
    self.goal = float(goal)

We also need to add the following to our update_balance() function: open the file in write mode, while we're in the loop write each account's name, balance and goal back into the file, then close the file when we're done.

CREATE
First, let's fix the datatype bug.

Find the __init__ function in the Account class, and wrap the balance and goal values in float() like we showed above.
In the update_balance() function, below balance_string = "", open accounts.txt in write mode and call it account_file.
Inside the for loop in this function, at the bottom, write() the details for the account into the file, separated by commas, i.e. {},{},{}\n and format it with the account's name, balance and goal.
At the very end of the function, below where account_details is set, close the file.
Click RUN to check the accounts list loads properly and make some deposits and withdrawals. If all goes well, when you close the app and then run it again, the balances should be saved!
'''

####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk
import random


##################  CLASS CODE  ######################
# Create the Account class
class Account:
    """The Account class stores the details of each account and has methods to deposit, withdraw and calculate progress towards the savings goal"""

    def __init__(self, name, balance, goal):
        self.name = name
        self.balance = float(balance)
        self.goal = float(goal)
        account_list.append(self)

    # Deposit method adds money to balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    # Withdraw method subtracts money from balance
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            return True
        else:
            return False

    # Get progress method calculates goal progress
    def get_progress(self):
        progress = (self.balance / self.goal) * 100
        return progress


##############  FUNCTIONS AND SETUP ###############
# Create a function to read data from the file
def get_data():
    account_file = open("accounts.txt", "r")
    line_list = account_file.readlines()

    for line in line_list:
        account_data = line.strip().split(",")
        Account(*account_data)

    account_file.close()


# Create a function to get account names list
def create_name_list():
    name_list = []
    for account in account_list:
        name_list.append(account.name)
    return name_list


# Create a function that will update the balance.
def update_balance():
    total_balance = 0
    balance_string = ""
    account_file = open("accounts.txt", "w")

    # Append each accounts balance, progress and goal to the label
    for account in account_list:
        progress = account.get_progress()
        balance_string += "{}: ${:.2f} - {:.0f}% of ${:.2f} goal\n".format(account.name, account.balance, progress,
                                                                           account.goal)
        total_balance += account.balance
        account_file.write("{},{},{}\n".format(account.name, account.balance, account.goal))

    balance_string += "\nTotal balance: ${:.2f}".format(total_balance)
    account_details.set(balance_string)
    account_file.close()


# Create the deposit function
def deposit_money(account):
    if account.deposit(amount.get()):
        message = random.choice(deposit_messages)
        message_text.set(message)
        action_feedback.set("Success! Total of ${:.2f} deposited into {}".format(amount.get(), account.name))
        image_label.configure(image=happy_image)
    else:
        action_feedback.set("Please enter a positive number")


# Create the withdraw function
def withdraw_money(account):
    if account.withdraw(amount.get()):
        message = random.choice(withdraw_messages)
        message_text.set(message)
        action_feedback.set("Success! Total of ${:.2f} withdrawn from {}".format(amount.get(), account.name))
        image_label.configure(image=sad_image)
    else:
        action_feedback.set("Not enough money in {} or not a valid amount".format(account.name))


# Create the manage action function
def manage_action():
    try:
        for account in account_list:
            if chosen_account.get() == account.name:
                if chosen_action.get() == "Deposit":
                    deposit_money(account)
                else:
                    withdraw_money(account)

        # Update the GUI
        update_balance()
        amount.set("")

    # Add an exception for text input
    except ValueError:
        action_feedback.set("Please enter a valid number")


# Set up Lists
account_list = []
deposit_messages = ["Well done, keep those deposits coming!", "You're making good progress!",
                    "Awesome! It will feel great when you reach your goal"]
withdraw_messages = ["Think about where else you might be able to save some money this week",
                     "You're doing well, but try to keep that spending under control",
                     "Tomorrow is another day for saving!"]

# Create instances of the class
get_data()
account_names = create_name_list()

##################  GUI CODE  ######################
root = Tk()
root.title("Goal Tracker")

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Account Details")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="/images/python/neutral.png")
happy_image = PhotoImage(file="/images/python/happy.png")
sad_image = PhotoImage(file="/images/python/sad.png")

image_label = ttk.Label(top_frame, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and set the account details variable
account_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=account_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create a label for the account combobox
account_label = ttk.Label(bottom_frame, text="Account: ")
account_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(bottom_frame, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(bottom_frame, text="Action:")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create an action feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

# Run the mainloop
update_balance()
root.mainloop()
