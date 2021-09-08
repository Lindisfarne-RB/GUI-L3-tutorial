'''Adding an amount input to our goal tracking app
Let's return to our goal tracking app. We've got an area set up where our helpful goal tracking character welcomes us and tells us how much money we currently have.

We want our users to be able to deposit and withdraw money, so we're going to need an Entry widget where they can type in the amount. We're also going to need to label it so they know what to type into it.

Let's start with the label.'''
'''Under the relevant comment, create a Label called amount_label with root as parent and the text Amount:  This text won't change so we can hard-code it in rather than using a variable.'''
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
neutral_image = PhotoImage(file="smiley.png")
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

# Run the mainloop
root.mainloop()

