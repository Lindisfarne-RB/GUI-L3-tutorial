'''Adding a multiline label using \n
We will be building the GUI for our banking app in stages during these first 10 lessons, and we'll add the functionality in the second 10 lessons.

We now have a welcome message label and an image label, but this part of the GUI will need one more label to show us our account balances. So let's get one more bit of practice adding a label with a textvariable.

This time, instead of using wraplength we're going to split the label onto 2 lines using \n, which is the newline character.'''
'''Under the relevant comment, create a StringVar() called account_details.
Set account_details to: Savings: $500 - 25% of $2000 goal \nTotal balance: $500
Create a label called details_label and set the textvariable to account_details.
Pack the details label into the GUI.
'''

from tkinter import *

root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = Label(root, textvariable=message_text, wraplength=250, justify="center")
message_label.pack()

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="call.png")
image_label = Label(root, image=neutral_image, justify="center")
image_label.pack()

# Create and set the account details variable
account_details = StringVar()
account_details.set("Savings: $500 - 25% of $2000 goal \nTotal balance: $500")

# Create the details label and pack it into the GUI
details_label = Label(root, textvariable=account_details)
details_label.pack()

# Run the mainloop
root.mainloop()
