'''Getting to know the Entry widget.
A widget that is commonly needed in a GUI app is an Entry widget. This is a basic text input field that the user can type into. Let's see how it works:

name_entry = Entry(root, textvariable=name, width=30)
Usually, we would have it linked to a variable because we most likely want to do something with the value. The width for an entry is measured in characters by default.

In the editor is our practice GUI we have been working with. We will come back to this one regularly to learn new skills before we put them into the actual goal tracking app GUI.'''

'''Under the relevant comment, create a StringVar() called words, we don't need to set a value this time.
Under the next comment, create an Entry called words_entry with root as parent, and set the textvariable to words.'''
from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = Label(root, text="My GUI App!")
label1.pack()

#Create a StringVar() to store text
words = StringVar()

# Create a text entry field

words_entry = Entry(root, textvariable=words, width=15)
words_entry.pack()
# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, text="Another label", wraplength=150)
label2.pack()

# Run the main window loop
root.mainloop()