'''Reducing the risk of bugs in GUI code
Here's a quick tip: you can use a loop to configure any grid() properties, including padding and sticky, on all children of a widget at once by accessing them using winfo_children():
# Add padding to all children of root
for widget in root.winfo_children():
  widget.grid(padx=10, pady=5)
This is a good idea when you have an interface with a lot of widgets as it means you don't have to worry about polishing the layout of your GUI each time you create a widget. Instead, you can take care of it all at the end right before you call mainloop().

It also means if you change your mind and want to modify the layout later, you can change these values just once rather than for all, say, 10 widgets.

CREATE
Under the relevant comment, just before mainloop() write a for loop statement that will loop through each widget in root's winfo_children().
Inside the loop, use grid() to add 10px padding to the sides and 5px padding to the top and bottom of the widget.'''


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
greeting_label.grid(row=2, column=0)

# Create a label for the user's name
name_label = ttk.Label(root, textvariable=name)
name_label.grid(row=2, column=1, padx=10, pady=10)

# Add padding to all children of root
for widget in root.winfo_children():
  widget.grid(padx=10, pady=5)

# Run the main window loop
root.mainloop()
