'''from tkinter import *
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

# Create a second label with longer text and add it to the window using pack()
greeting_label = ttk.Label(text="Hello", wraplength=150)
greeting_label.grid(row=1, column=0)

# Create a label for the user's name
name_label = ttk.Label(root, variable=name)
name_label.grid(row=2, column=1, padx=10, pady=10)

# Run the main window loop
root.mainloop()
Debugging GUI code part 2
Ok, next let's look at some bugs that are common to tkinter code specifically:

Forgetting to specify the parent widget, or specifying the wrong parent
Forgetting to put the widget into the window using pack() or grid()
Not running .mainloop() on the window, or running it before all of the widgets have been added
Using the wrong rows and columns in .grid()
Mixing up parameters like variable and textvariable
CREATE
We've added a couple more widgets now

Something is missing from line 20–find the bug!
For some reason the name_entry won't show up–check the grid values for all the widgets and find the bug!
Is that the right argument on line 24 for the name label? Fix the bug!'''


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

# Create a second label with longer text and add it to the window using pack()
greeting_label = ttk.Label(root, text="Hello", wraplength=150)
greeting_label.grid(row=1, column=0)

# Create a label for the user's name
name_label = ttk.Label(root, textvariable=name)
name_label.grid(row=2, column=1, padx=10, pady=10)

# Run the main window loop
root.mainloop()
