'''The Combobox widget
Ttk also has a ComboBox() widget class which is like an OptionMenu combined with an Entry so the user can select an option or type in a value. A combobox can also be set to readonly to disable free input and make the user choose from the list:

options = ['Vanilla', 'Strawberry', 'Chocolate']
my_variable = StringVar()
my_variable.set(options[0])

my_combobox = ttk.Combobox(root, textvariable=my_variable, state="readonly")
my_combobox['values'] = options
We give it the same information as an option menu but in a slightly different way, as you can see above. There's no default option so we would set the my_variable variable to the value we want selected first. We pass in the variable as a textvariable and set the 'values' for the menu after.

CREATE
In our goal tracking app we want drop downs to choose which account we want to use, and also which action we want to do - deposit or withdraw. We will add these above the amount entry. Let's start with the account label.

Change the GUI position of amount_label to row 5 and submit_button to row 6 to make room for the 2 rows we will be adding to the GUI.
Under the relevant comment, create a label for the account Combobox called account_label with the text Account:  and place it in row 3, column 0 of the GUI
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
neutral_image = PhotoImage(file="pattern.png")
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
