'''Using a StringVar() to set the text for a label
At the moment, we are hard-coding the text for our labels. This is fine when we know that our label text will never change.

Sometimes, however, we might want the label text to change when the user does something. To do this, we can use a tkinter variable. Tkinter handles variables a bit differently from regular Python code. You have to decide the datatype first, then create the right variable and set the value:
name = StringVar()
name.set("Billy")
my_label = Label(root, textvariable=name)
Then, instead of setting a text parameter, we set a textvariable parameter in our label.

Whatever value is stored in the name variable will be displayed in the label. If the name variable changes at all, the label will automatically be updated which is pretty cool!'''

'''In this course we are going to build a banking type app that lets the user deposit and withdraw money from accounts, and track progress towards savings goals such as a holiday, or new video game console. Click here for more detail. We've put an empty window in the code for you to start with.

Change the title of the window to Goal Tracker.
Under the relevant comment, create a StringVar() called message_text.
On the next line, set() the variable message_text to: Welcome! You can deposit or withdraw money and see your progress towards your goals.
Under the next relevant comment, create a label called message_label with root as the parent, message_text as the textvariable and a wraplength of 250.
Pack the message label into the GUI.

Note: In tkinter we can have: StringVar(), IntVar(), DoubleVar() or BooleanVar(). A DoubleVar() is just another name for a float variable.'''

'''
How can we help you?
 
GOAL TRACKING APP

The app we build in this course isn't designed to be an actual banking program, as most people would just use their online banking for that, but rather an app for tracking progress toward some goals.

Although in the course we use accounts and depositing and withdrawing money, the code could easily be adapted for other apps. For example, it could be turned into an app for parents to track their children's saving progress for a new toy or bike with money from their allowance and chores.

It could also be modified to track time spent doing activities like practice or exercise, calories consumed or credits earned from courses. So, once you've completed the course, get creative with the code and let us know what you come up with'''

from tkinter import *

# Create a window
root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals")
message_label = Label(root, textvariable=message_text, wraplength =250)


# Create the message label and add it to the window using pack()
message_label.pack()


# Run the main window loop
root.mainloop()


