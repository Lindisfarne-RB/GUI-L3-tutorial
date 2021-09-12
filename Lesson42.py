'''Debugging GUI code part 1
You've made it to the last lesson in the GUI part of the course! In this lesson we're going to take a look at some common bugs we might come across in GUI code. Let's start with the bugs we've seen in levels 1 and 2 already:

Using the wrong quotes "" or forgetting to close them
Using the wrong brackets () or forgetting to close them
Using the wrong case i.e. UPPER vs. lower case letters
Forgetting to import a module you need like tkinter or ttk
CREATE
It's time for a bug hunt!

Something is missing from line 2–fix the bug!
There's a bug on line 9 that means our label isn't working properly, see if you can fix it.
There's something wrong with one of the arguments for the Entry widget on line 16. Fix the bug.
Hmm, what has gone wrong on line 17? Find the bug and fix it!
'''

'''Find bugs here
from tkinter import *


# Create a window
root = Tk()
root.title("Greetings App")

# Create a label and add it to the window using pack()
title = ttk.label(root, text="Greetings! Enter your name: ")
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#Create a StringVar() to store text
name = StringVar()

# Create a text entry field
name_entry = ttk.Entry(root, textvariable="name")
name_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10

# Run the main window loop
root.mainloop()
'''

'''Solution'''
 

from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("Greetings App")

# Create a label and add it to the window using pack()
title = ttk.Label(root, text="Greetings! Enter your name: ")
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#Create a StringVar() to store text
name = StringVar()

# Create a text entry field
name_entry = ttk.Entry(root, textvariable=name)
name_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run the main window loop
root.mainloop()