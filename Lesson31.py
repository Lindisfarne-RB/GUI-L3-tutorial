'''8.2
Using a variable with a Checkbutton widget
We can assign a variable to a Checkbutton which will keep track of whether the box is checked or not. This variable is usually an IntVar() because by default the values used are 0 for unchecked and 1 for checked:
my_checkvar = IntVar()
my_checkbutton = ttk.Checkbutton(root, text="Tick me!", variable=my_checkvar)Click here for some more detail on this

If you want to check or uncheck a checkbutton at any point in a program, you can set the value of the variable to the onvalue or offvalue, for example:
my_checkvar.set(1) # Checks the box
my_checkvar.set(0) # Unchecks the box
You can also use command to run a function when the checkbutton is checked or unchecked.

CREATE
We have added a small function called check() that just prints the value of check1_var to the console when the checkbutton is clicked. Complete these tasks under the relevant comment:

Create an IntVar() called check1_var.
Add this variable to the check1 checkbutton.
Create another IntVar() called check2_var.
Add this variable to the check2 checkbutton.
Underneath where you created check2_var, make it so that check2 is already checked when the window loads, but still disabled.
Add a command to check1 that will run the check() function.'''

from tkinter import *
from tkinter import ttk


# Click function
def check():
    print(check1_var.get())


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

# Create variables for 2 checkbuttons
check1_var = IntVar()
check2_var = IntVar()
check2_var.set(1)

# Create 2 check buttons
check1 = ttk.Checkbutton(frame3, text="Option 1", variable=check1_var, command=check)
check1.grid(row=0, column=0)

check2 = ttk.Checkbutton(frame3, text="Option 2", variable=check2_var, state="disabled")
check2.grid(row=1, column=0)

# Run the main window loop
root.mainloop()
