'''LESSON 8.1
LEARN
The Checkbutton widget
We're going to take a short break from our goal tracking app to have a look at a couple of widgets that we haven't used in that program, but that are very useful.

The first is the Checkbutton widget. A checkbutton lets you toggle a choice for something, and if you have a group of checkbuttons then the user can select more than one option.

Here is the basic syntax for a checkbutton:
my_checkbutton = ttk.Checkbutton(root, text="Tick me!")
We can disable the checkbutton using state="disabled" and assign it a variable, which we will do in the next task.

CREATE
We have added a LabelFrame called frame3 to the GUI, so put these checkbuttons inside that frame.

Under the relevant comment, create a checkbutton called check1 inside frame3, with the text Option 1.
Place this Checkbutton at row 0, column 0.
Create a second Checkbutton called check2 also inside frame3 with the text Option 2.
Disable check2 using the state argument.
Place check2 in row 1, column 0.
Click RUN to see the updated GUI.
TIPS
Some differences between tkinter and ttk Checkbuttons.

'''
from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("My GUI App")

# Create a frame for first 2 widgets
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0)

# Create a label and add it to the window using pack()
label1 = ttk.Label(frame1, text="My GUI App!")
label1.grid(row=0, column=0, padx=10, pady=5)

# Create a StringVar() to store text
words = StringVar()

# Create a text entry field
words_entry = ttk.Entry(frame1, textvariable=words)
words_entry.grid(row=1, column=0, padx=10, pady=5)

# Create a frame for the second 2 widgets
frame2 = ttk.Frame(root)
frame2.grid(row=1, column=0)

# Create a second label with longer text and add it to the window using pack()
label2 = ttk.Label(frame2, textvariable=words, wraplength=150)
label2.grid(row=2, column=0, padx=10, pady=5)

# Create a StringVar() for the chosen option
chosen_option = StringVar()

# Create a list of items for the Option Menu
options = ['Vanilla', 'Strawberry', 'Chocolate']

# Create the option menu and place in row 3, column 0
option_menu = ttk.OptionMenu(frame2, chosen_option, options[0], *options)
option_menu.grid(row=3, column=0, padx=10, pady=5)

# Create a LabelFrame for the checkbuttons
frame3 = ttk.LabelFrame(root, text="Checkbuttons")
frame3.grid(row=2, column=0, padx=10, pady=10, sticky="WE")

# Create 2 check buttons

check1 = ttk.Checkbutton(frame3, text="Option 1")
check1.grid(row=0, column=0)

check2 = ttk.Checkbutton(frame3, text="Option 2", state="disabled")
check2.grid(row=1, column=0)

# Run the main window loop
root.mainloop()
