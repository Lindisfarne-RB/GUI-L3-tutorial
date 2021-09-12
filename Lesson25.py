''' LESSON 6.4
LEARN
Adding an "action" Combobox to our goal tracking UI
Now that we have added the account drop down menu to the GUI we'll need to add a second one. This second drop down menu will allow the user to choose to either "deposit" or "withdraw" money. Right now we'll create the drop down menu and place it into our GUI. Later, we'll add the code to make it work properly.

CREATE
Complete the following tasks under the relevant comments:

Create a label for the action Combobox called action_label with the text Action:  and place it in row 4, column 0.
Create a list called action_list for the options Deposit, Withdraw.
Create a string variable for the Combobox called chosen_action.
Set the variable to the first option in the action_list.
Create a readonly ttk Combobox called action_box using the variable.
Set the values for the Combobox to the action_list
Place the action_box in row 4, column 1 and add 10px padding to the sides and 3px padding top and bottom.
Click RUN to test out the updated GUI.
TIPS
Note that the app will still only deposit money into the savings account at this stage. We will fix this later on.

'''

from tkinter import *
from tkinter import ttk

# Create a variable to store the account balance
savings_balance = 0


# Create a function that will update the balance.
def update_balance():
    global savings_balance
    deposit_amount = amount.get()
    savings_balance += deposit_amount
    total_balance = savings_balance
    account_details.set("Savings: ${:.2f}\nTotal Balance: ${:.2f}".format(savings_balance, total_balance))
    amount.set("")


root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = ttk.Label(root, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="smiley.png")
image_label = ttk.Label(root, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and set the account details variable
account_details = StringVar()
account_details.set("Savings: $0 \nTotal balance: $0")

# Create the details label and pack it into the GUI
details_label = ttk.Label(root, textvariable=account_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label for the account combobox
account_label = ttk.Label(root, text="Account: ")
account_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
account_names = ["Savings", "Phone", "Holiday"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(root, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=3, column=1, padx=10, pady=3)

# Create a label for the action Combobox
action_label = ttk.Label(root, text="Action:")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(root, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3)

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3)

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=update_balance)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the mainloop
root.mainloop()
