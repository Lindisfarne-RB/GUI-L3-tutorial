'''Making a button call a function
At the start of this lesson we talked about making something happen when a user clicks a button. This is commonly called handling an event in programming.

In a Button widget, we can set a command argument that will call a function when the button is clicked:
def say_hello():
    label_text.set("Hello!")

label_text = StringVar()
my_label = ttk.Label(root, textvariable=label_text)
my_button = ttk.Button(root, text="Click Me!", command=say_hello)
In this code, we have created a function called say_hello() that changes the label text to Hello. When the button is clicked, this function is called.

If you need to get the value of a variable, for example from an Entry, you can use the .get() function e.g. a_value = a_variable.get()

Let's add a function and a call to it in our goal tracking app. We want the user to enter an amount, click "submit" and have that amount added to their savings account balance.

CREATE
First, we'll need a variable to store the account balance. On line 5 create a regular python variable called savings_balance and set it to 0.
Next, create a function called update_balance that takes no parameters.
Inside the function, add the line global savings_balance - this lets us access the savings balance variable inside the function, without having to pass it in.
Then use the .get() function to get the value in the amount entry, and store it as deposit_amount.
Add the deposit amount to the current savings balance, and store in savings_balance.
Add a command to the submit_button to run the update_balance() function when clicked.
TIPS
Note: When you write the name of a function in a command argument, you don't include the () brackets.

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


# GUI Code
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


