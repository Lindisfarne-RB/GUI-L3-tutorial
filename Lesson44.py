'''from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("Greetings App")

# Create a label and add it to the window using pack()
title = ttk.Label(root, text="Greetings! Enter your name: ")
title.grid(row=0, column=0, columnspan=2)

#Create a StringVar() to store text
name = StringVar()

# Create a text entry field
name_entry = ttk.Entry(root, textvariable=name)
name_entry.grid(row=1, column=0, columnspan=2)

# Create a second label with longer text and add it to the window using pack()
greeting_label = ttk.Label(root, text="Hello", wraplength=150)
greeting_label.grid(row=2, column=0)

# Create a label for the user's name
name_label = ttk.Label(root, textvariable=name)
name_label.grid(row=2, column=1)

# Run the main window loop
root.mainloop()
'''




from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("Greetings App")

# Create a label and add it to the window using pack()
title = ttk.Label(root, text="Greetings! Enter your name: ")
title.grid(row=0, column=0, columnspan=2)

# Create a StringVar() to store text
name = StringVar()

# Create a text entry field
name_entry = ttk.Entry(root, textvariable=name)
name_entry.grid(row=1, column=0, columnspan=2)

# Create a second label with longer text and add it to the window using pack()
greeting_label = ttk.Label(root, text="Hello", wraplength=150)
greeting_label.grid(row=2, column=0)

# Create a label for the user's name
name_label = ttk.Label(root, textvariable=name)
name_label.grid(row=2, column=1)

# Run the main window loop
root.mainloop()

'''Looking for bugs that don't break your code
It can also be easy to mess up your GUI code if you try to add padding to your widgets later on and you miss some out, or put the wrong amount on them.

CREATE
Oops, we were supposed to put 5px padding on the top and bottom of all of the widgets, but we left out one of them, and we put 10 on the others. Let's refactor this code using a loop and winfo_children().

Which widget has no padding on it? 
Delete the padx and pady values for all of the other widgets.'''