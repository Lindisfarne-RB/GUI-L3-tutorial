'''Customizing an Entry widget
We have seen that we can change the width of an Entry widget. Like a label, there are many other things that can be customized too. Again, just because you can change the colors of things, it doesn't mean you should, but here are a couple of examples:

colorful_entry = Entry(root, bg="blue", fg="yellow", selectbackground="limegreen", selectforeground="black")
bg and fg set the background color of the entry box and the color of the text in the entry box respectively.
selectbackground sets the highlight color of selected text in the entry and selectforeground sets the color of text itself when it is selected.'''

'''Set the background color of the words_entry widget to a color of your choice e.g. yellow.
Set the foreground color of the words_entry widget to another color of your choice.
Set the background color for selected text to another color of your choice.
Set the text color for selected text to another color of your choice.'''

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
words_entry = Entry(root, textvariable=words, bg="yellow", fg="red" ,selectbackground="limegreen", selectforeground="black")
words_entry.pack()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, textvariable=words, wraplength=150)
label2.pack()

# Run the main window loop
root.mainloop()

