'''More on creating a label
In the first lesson we had a look at how to create a window and add a label. In this lesson we are going to take a closer look at labels!

When we create a label, there are a few other parameters we can set in addition to the parent and the text. Let's look at some:

my_label = Label(root, text="Here is a label with a long sentence in it", wraplength=100, justify="center", fg="red", bg="yellow")
wraplength says how wide each line should be. We can use this to make a longer label wrap onto multiple lines. By default this is measured in pixels.
justify lets you set the text to be left, right or center aligned within the label. By default, all text in a label is centered.
fg sets the foreground color or text color for the writing in the label.
bg sets the background color for the space that the label takes up behind the text.
'''

'''CREATE
Set the background color for label1 to blue.
Set the foreground color for label1 to yellow.
Set the wraplength for label2 to 100.
Left align the text in label2.
Click RUN to see the updated GUI.'''

from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = Label(root, text="My GUI App!",bg="blue",fg="yellow")
label1.pack()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, text="Whatever you want but make it a longer sentence!", wraplength=100,justify="left")
label2.pack()

# Run the main window loop
root.mainloop()