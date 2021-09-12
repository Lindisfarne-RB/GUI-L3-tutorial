''' LESSON 6.1
LEARN
Drop-down menus: the OptionMenu() widget
We now have a bit more control over our GUI using the .grid() geometry manager, so let's have a look at some more widget types.

Drop-down menus are common in GUI apps, and both tkinter and ttk give us the OptionMenu() widget class to use for this:

my_menu = ttk.OptionMenu(root, my_variable, default_option, *options)
With a ttk option menu there are 4 bits of information that are needed:

The parent widget, in this case root
A variable to store the chosen value in, in this case my_variable
The value you want to be selected when the window loads
A list of options that the user can choose from, in this case a list called options that might look like this:
options = ['Vanilla', 'Strawberry', 'Chocolate']
We pass the list in with an argument with a * at the start.

CREATE
Let's get some practice using our demo GUI app.

Under the relevant comment, create a StringVar() called chosen_option to store the user's choice.
Under the next comment, create a list called options with at least 3 items to be the options for the menu. You can use any items you like - flavors, cars, movies, numbers...
Now, create a ttk OptionMenu called option_menu under the next comment. It should have root as parent, the variable we created, the first item of options as the default option and the options list passed in.
Place the option_menu in row 3 and column 0, and give it 5px padding top and bottom and 10px on the sides.'''

from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = ttk.Label(root, text="My GUI App!")
label1.grid(row=0, column=0, padx=10, pady=5)

#Create a StringVar() to store text
words = StringVar()

# Create a text entry field
words_entry = ttk.Entry(root, textvariable=words)
words_entry.grid(row=1, column=0, padx=10, pady=5)

# Create a second label with longer text and add it to the window using pack()
label2 = ttk.Label(root, textvariable=words, wraplength=150)
label2.grid(row=2, column=0, padx=10, pady=5)

# Create a StringVar() for the chosen option
chosen_option = StringVar()

# Create a list of items for the Option Menu
options =['Vanilla', 'Strawberry', 'Chocolate']

# Create the option menu and place in row 3, column 0

option_menu = ttk.OptionMenu(root, chosen_option, options[0], *options)
option_menu.grid(row=3, column=0, padx=10, pady=5)


# Run the main window loop
root.mainloop()
