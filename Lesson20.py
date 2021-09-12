'''Laying out our goal tracking GUI with .grid()
Ok, let's use .grid() to improve the layout of our app GUI!

It would be nice if we could sit the Amount:  label and its entry box next to each other on one line, as later we will need to add some other widgets to choose an account and so on.

In that row, we will have 2 columns, so we will need to set the columnspan of all of the other widgets to 2.

Here are the positions each widget should be in:

message_label: row 0, column 0
image_label: row 1, column 0
details_label: row 2, column 0
amount_label: row 3, column 0
amount_entry: row 3, column 1
submit_button: row 4, column 0
CREATE
Position each widget in the positions listed above using .grid() instead of .pack().
Set the columnspan for all widgets except amount_label and amount_entry to 2.
Click RUN to see the updated GUI.
TIPS
Ok, it's not perfect yet but we will polish it up some more in the next task!

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
message_label.grid(row = 0, column = 0, columnspan=2)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="pattern.png")
image_label = ttk.Label(root, image=neutral_image)
image_label.grid(row =1, column= 0, columnspan=2)

# Create and set the account details variable
account_details = StringVar()
account_details.set("Savings: $0 \nTotal balance: $0")

# Create the details label and pack it into the GUI
details_label = ttk.Label(root, textvariable=account_details)
details_label.grid(row =2, column= 0,columnspan=2)

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row =3, column= 0)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.grid(row=3, column =1)

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=update_balance)
submit_button.grid(row =4, column =0, columnspan=2)

# Run the mainloop
root.mainloop()



