'''Adding the amount entry field
Ok, now we need to create a variable so that we can store the value the user types in, and create the Entry field itself.

Users might want to enter an amount like $65.50 so we'll need to use a DoubleVar() which will let us store float values. When we do this, it puts the value 0.0 into the field. It will be annoying if the user has to delete this before they start typing, so we're going to set() the variable to an empty string "" to start off with so that the field will be empty.

Let's do it!'''
'''Create a DoubleVar() called amount under the relevant comment.
Set amount to an empty string by putting "" inside the brackets of the set() function.
Under the next comment, create an Entry called amount_entry with root as parent and amount as the textvariable.
Pack amount_entry into the GUI.'''

from tkinter import *

root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = Label(root, textvariable=message_text, wraplength=250)
message_label.pack()

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="snapchat.png")
image_label = Label(root, image=neutral_image)
image_label.pack()

# Create and set the account details variable
account_details = StringVar()
account_details.set("Savings: $500 - 25% of $2000 goal \nTotal balance: $500")

# Create the details label and pack it into the GUI
details_label = Label(root, textvariable=account_details)
details_label.pack()

# Create a label for the amount field and pack it into the GUI
amount_label = Label(root, text="Amount:")
amount_label.pack()

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = Entry(root, textvariable = amount)
amount_entry.pack()

# Run the mainloop
root.mainloop()


