'''16.2Writing the beginning of the deposit function
We've got some messages to select from randomly when the user deposits or withdraws money, so now let's write our deposit function. We're going to call it deposit_money() and here is an outline of what we want it to do:
Get the chosen account as a parameter
If depositing the amount is successful
  Choose a random deposit message
  Set the message text area to the message
Because our deposit() method returns True or False, we can put the call to the method in an if statement to see if it is successful:
if account.deposit(amount.get()):
  #Do stuff
Note that we're also using .get() to get the amount the user has entered into the entry field.

CREATE
Complete these steps under the relevant comment on line 60.

Create a function called deposit_money() which takes one parameter account.
Write an if statement that checks whether depositing the amount into the chosen account is successful.
Add the pass  keyword inside the if statement for now and click CHECK.
TIPS
We need to use the random module to pick a message, so we'll do that in the next task.

'''
####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk


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
        balance_string += "{}: ${:.2f} - {:.0f}% of ${} goal\n".format(account.name, account.balance, progress,
                                                                       account.goal)
        total_balance += account.balance

    balance_string += "\nTotal balance: ${:.2f}".format(total_balance)
    account_details.set(balance_string)


# Create the deposit function
def deposit_money(account):
    if account.deposit(amount.get()):
        pass


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
neutral_image = PhotoImage(file="smiley.png")
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
submit_button = ttk.Button(bottom_frame, text="Submit", command=update_balance)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the mainloop
update_balance()
root.mainloop()





