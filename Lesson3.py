'''Adding a label to the window
Ok, we've got a window, but that's not very exciting by itself! So, let's look at how to add our first widget - a Label.

There are 2 basic steps for adding a widget in tkinter:
my_label = Label(root, text="My Label")
my_label.pack()
First, we create the label, giving it a name. The parameters in the brackets say that root is the parent widget, in other words that this label should go inside the root window, and that the text on the label should be My Label.

The second line uses the pack() function to actually put the widget into the window. We will learn more about ways of doing this later, but for now just know that pack() puts each widget into the window after any that have already been packed.'''

'''Under the relevant comment in the editor, create a label called label1, with parent root and text My GUI App!
On the next line, add label1 to the window using pack().
Click RUN to see the window with the new label added.
Under the next comment, create a label called label2, with parent root also, but this time make the text a longer sentence–it can say anything.
Pack the label into the window.
Click RUN to see what happens now that we have a label with longer text.
'''

from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = Label(root, text="My GUI App!")
label1.pack()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, text="My Longer Label")
label2.pack()


# Run the main window loop
root.mainloop()


