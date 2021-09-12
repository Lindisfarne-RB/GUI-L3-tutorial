'''LESSON 9.4
LEARN
Adding branches for the other accounts
The next step in our function is to repeat the same process for the other 2 accounts. Now, this is an example of something that breaks a golden rule of programming which is: DRY. DRY stands for Don't Repeat Yourself! We have already learned about this when we looked at loops in Python level 1 and functions in Python level 2.

You can probably see that if we wanted to add a fourth account, we'd also have to repeat all of the code again! At this stage, our skills are a bit too limited to avoid this kind of repetition. In lessons 11-20 we will learn how to deal with this by making our accounts into objects. For now, we'll just have to repeat the code to get our app working.

CREATE
Add an elif branch to the outside if statement that checks if the account is Phone this time.
Repeat the code from inside the Savings branch, but add/subtract the amount from phone_balance this time.
Add another elif branch that checks if the account is Holiday.
Repeat the code from inside the Phone branch, but add/subtract the amount from the holiday_balance variable.
'''
from tkinter import *
from tkinter import ttk

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
