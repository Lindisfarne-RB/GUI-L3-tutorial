'''Creating Radiobutton widgets
Similar to the Checkbutton is the Radiobutton. The main difference between these widgets is that radiobuttons come in groups, and you can only select one of the options.

The basic syntax for a radio button is this:

my_radiobutton = ttk.Radiobutton(root, text="Choose me!", variable=my_radiovar, value=1, command=do_something)
We give the button text, assign a variable, and set a value which should match the datatype of the variable. We can also add a command just like a Checkbutton.

CREATE
We've added frame4 for you to put the radiobuttons inside.

Under the relevant comment, create a new StringVar() called radio_var that will go with our radiobuttons.
Under the next comment, create a radiobutton called radio1 inside frame4 with the text Red and value red.
Add the variable radio_var to this radio button.
Place it in the frame in row 0, column 0.
Now create another radio button called radio2 but for the color Green and place it in row 0, column 1.
Lastly, create a third radio button called radio3 for Blue and place it in row 0, column 2.
Click RUN to see the updated GUI.
(Optional) You could add some padding to each radiobutton to space them out if you'd like to.
TIPS
Note: All 3 radiobuttons should use the same variable radio_var.'''

from tkinter import *
from tkinter import ttk


# Check function
def check():
    print(radio_var.get())


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

# Create a LabelFrame for the radiobuttons
frame4 = ttk.LabelFrame(root, text="Radiobuttons")
frame4.grid(row=3, column=0, padx=10, pady=10, sticky="WE")

# Create 3 radiobuttons
radio_var = StringVar()
radio1 = ttk.Radiobutton(frame4, text="Red", value="red", variable=radio_var)
radio1.grid(column=0, row=0)

radio2 = ttk.Radiobutton(frame4, text="Green", value="green", variable=radio_var)
radio2.grid(column=1, row=0)

radio3 = ttk.Radiobutton(frame4, text="Blue", value="blue", variable=radio_var)
radio3.grid(column=2, row=0)

# Run the main window loop
root.mainloop()
