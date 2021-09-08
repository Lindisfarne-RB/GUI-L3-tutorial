'''Themed tkinter widgets or ttk
If you put tkinter code into a Python editor on your computer such as IDLE or PyCharm and run it, you might be disappointed with how plain the GUI looks. This might make you want to brighten it up with some colors and things like we did with our submit button. However, as we've mentioned, users generally want a GUI to look nice, but also consistent with the operating system they are using.

Luckily, tkinter has a collection of themed widgets, called ttk that can be imported if you want a simple way to make your GUI look nicer. These widgets are designed to look more native, so if you're on Windows they will be styled like the normal Windows programs, if you're on Mac, they'll be styled to look like Mac programs (click to enlarge):'''
'''check themed ttk image here
To use ttk widgets, you just import them and then use ttk. in front of your widgets:
from tkinter import ttk
my_button = ttk.Button(root, text="Hello")
Note that you can't set parameters like bg and fg on these. There are a few other differences between tk and ttk widgets, but we will explain them as they come up in the course.'''
'''We've prefixed the Labels for you–they don't really look much different as ttk widgets, but it's good to be consistent.

Import ttk from tkinter on line 2 of our goal tracking app code.
On line 37, put the ttk. prefix in front of the amount_entry widget.
On line 41, put the ttk. prefix in front of the submit_button widget.'''
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the message label
message_label = ttk.Label(root, textvariable=message_text, wraplength=250)
message_label.pack()

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="images/themed ttk 2.png")
image_label = ttk.Label(root, image=neutral_image, width=25)
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
submit_button = ttk.Button(root, text="Submit")
submit_button.pack()

# Run the mainloop
root.mainloop()


