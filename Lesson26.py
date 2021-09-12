'''LESSON 7.1

Using frames to organize more complex layouts
Tkinter and ttk give us some nice ways of grouping related widgets in a GUI: frames and labelframes.

A frame is just a rectangular container that you can put widgets inside by using the frame as the widgets' parent instead of root:
my_frame = ttk.Frame(root)
my_frame.grid(row=0, column=0, sticky="NSEW")

my_button = ttk.Button(my_frame, text="Click me!")
my_button.grid(row=0, column=0)
You can then position the frame where you'd like it to go. In this case, we put it at row 0, column 0. Each frame has its own grid inside, so the first widget inside the frame can also be placed at row 0, column 0 because the counting starts again.

Let's have a look at our demo app.

CREATE
Complete the following tasks under the relevant comments:

Create a frame called frame1 with root as the parent.
Place the frame at row 0, column 0.
Change the parent of label1 and words_entry to frame1 instead of root.
Create another frame under the next relevant comment called frame2 with root as the parent.
Place the frame at row 1, column 0.
Put label2 and option_menu inside this frame.
Click RUN to see the updated GUI.
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

# Run the main window loop
root.mainloop()

