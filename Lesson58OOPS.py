'''Combining our Account class with the GUI code
We've now completed our Account class and we've learned how to create instances of it, or objects. We also know how to access the attributes and methods of an object by using dot notation:
#Create instance of account
savings = Account("Savings", 0, 1000)
# Call a method - deposit $50
savings.deposit(50)
# Access an attribute - print the balance
print(savings.balance)
That is most of what we need to know about how classes work at this stage, so the next step will be combining our class with our Goal Tracker program. This will help to develop an understanding of how object-oriented code works well with the event driven programming we get from our GUI.

The next few lessons will require a bit of refactoring of the code. If it gets confusing, just try to think carefully about what we are trying to do in each step.'''

'''In the editor, we have added the class code we created in the previous lessons to the GUI code, but we've deleted the code that was just for testing.
Read through the code to remind yourself of how it is put together.
We have added #### comments #### to divide up the sections into IMPORTS, CLASS CODE, FUNCTIONS AND SETUP, and GUI CODE. Replace the ???s in the comments with the correct labels.'''
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


##############  FUNCTIONS AND SETUP #################
# Create a variable to store the account balance
savings_balance = 0
phone_balance = 0
holiday_balance = 0


# Create a function that will update the balance.
def update_balance():
 global savings_balance, phone_balance, holiday_balance
 account = chosen_account.get()
 mode = chosen_action.get()

 if account == "Savings":
     if mode == "Deposit":
         savings_balance += amount.get()
     else:
         savings_balance -= amount.get()

 elif account == "Phone":
     if mode == "Deposit":
         phone_balance += amount.get()
     else:
         phone_balance -= amount.get()

 elif account == "Holiday":
     if mode == "Deposit":
         holiday_balance += amount.get()
     else:
         holiday_balance -= amount.get()

 total_balance = savings_balance + phone_balance + holiday_balance
 balance_string = "Savings: ${:.2f}\nPhone: ${:.2f}\nHoliday: ${:.2f}\nTotal balance: ${:.2f}".format(
     savings_balance, phone_balance, holiday_balance, total_balance)
 account_details.set(balance_string)
 amount.set("")


# Create instances of the class
savings = Account("Savings", 0, 1000)
phone = Account("Phone", 0, 800)
holiday = Account("Holiday", 0, 7000)

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
account_details.set("Savings: $0 \nPhone: $0\nHoliday: $0\nTotal balance: $0")

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
account_names = ["Savings", "Phone", "Holiday"]
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
root.mainloop()

