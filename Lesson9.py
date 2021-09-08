'''Linking an Entry with a Label using a textvariable
Whenever the user types something into the Entry field, that value will be stored in the textvariable we have assigned to it.

We can link another widget to the same textvariable to see this in action. This is an easy way to use the value, and we will look at other ways later on.'''

'''Replace the ??? on line 19 to set the textvariable for label2 to words as well.
Click RUN and type some text into the entry field to see what happens!
(Optional) You may like to try changing the wraplength on label2 to some different numbers to see what happens to the label and the window when you enter more text in the entry field. What happens if you remove wraplength altogether?'''

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
words_entry = Entry(root, textvariable=words)
words_entry.pack()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, textvariable=words, wraplength=150)
label2.pack()

# Run the main window loop
root.mainloop()