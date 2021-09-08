'''Customizing a Button widget
Let's have a look at some of the things we can customize on a Button widget. We have bg and fg as usual, and here are a few others:

my_button = Button(root, text="Click Me!", bg="red", fg="yellow", width=30, height=3, bd=1, state="normal", activebackground="green")
width is measured in characters.
height is measured in rows or lines of text.
bd sets the border width for the button in pixels, the default is 2px.
state lets you disable a button using state="disabled", the default is "normal".
activebackground and activeforeground set the colors for the button and text when the user is pressing down on the button.'''
'''Set the width of the submit button to 16.
Set the background color to red.
Set the text color to yellow.
Set the active background color to lawngreen.'''
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
neutral_image = PhotoImage(file="pattern.png")
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
submit_button = Button(root, text="Submit", width=16, bg="red", fg="yellow" , activebackground="lawngreen")
submit_button.pack()

# Run the mainloop
root.mainloop()





