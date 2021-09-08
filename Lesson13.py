'''Creating a Button widget
Now that we’ve learned how to put labels, images, and text entry fields into a window, we need to learn to create buttons. Later, we will learn how to make things happen when a user clicks on one of our buttons but for right now, here’s the code to create a button that says, “Click Me!”:

my_button = Button(root, text="Click Me!")

We simply give it a name, use the Button widget class and put some text on it.

Let's add a Submit button to our goal tracking app so that we can do something with the amount the user enters.'''

'''Underneath the comment on line 39, create a Button called submit_button with root as the parent.
Set the text for the button to Submit.
Pack the button into the GUI.
Click RUN to see the updated GUI.'''

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
account_details.set("Savings: $0 \nTotal balance: $0")

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
amount_entry = Entry(root, textvariable=amount)
amount_entry.pack()

# Create a submit button
submit_button = Button(root, text="Submit")
submit_button.pack()
# Run the mainloop
root.mainloop()

