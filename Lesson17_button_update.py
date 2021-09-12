'''Updating the GUI from the function
Lastly, we need to make it so that our label gets updated with the new account balance. This is just a simplified version of what our finished app will do, but it is enough to learn how buttons work for now.

Since our details_label has our savings balance and total balance, we'll need to set a variable for that. This part will make more sense once we add the ability to have more than one account/goal, but for now let's future-proof it.

CREATE
Inside the update_balance() function, create a variable called total_balance and set it equal to savings_balance since we only have one account for now.
Use the .set() function to set the account_details variable to the following string: Savings: ${}\nTotal Balance: ${}.
Use .format() to insert the values savings_balance and total_balance into the string.
Click RUN and try depositing some money into your savings!
(Optional) Set the amount variable back to an empty string "" so that the field clears when the user hits submit.
(Optional) Format the output so that the balances in the label display to 2dp.
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
message_label.pack()

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="call.png")
image_label = ttk.Label(root, image=neutral_image)
image_label.pack()

# Create and set the account details variable
account_details = StringVar()

account_details.set("Savings: $0 \nTotal balance: $0")

# Create the details label and pack it into the GUI
details_label = ttk.Label(root, textvariable=account_details)
details_label.pack()

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(root, text="Amount:")
amount_label.pack()

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.pack()

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=update_balance)
submit_button.pack()

# Run the mainloop
root.mainloop()


