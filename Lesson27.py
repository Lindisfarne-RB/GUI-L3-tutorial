
'''
Working with frames
In a tkinter frame you can set background colors and other things as parameters, but not with a ttk frame.

The good thing about frames is that if you need to rearrange your GUI, then you can just move the frames instead of each individual widget. In this task we're going to change our frames to tkinter frames and add background colors just so that we can see what is happening.

CREATE
Remove the ttk. prefix from frame1 and give it a background color e.g. red.
Do the same for frame2 but make it a different color e.g. blue.
Click RUN to see how the 2 frames are laid out in the GUI.
They're not quite the same size, and if you type into the field until frame2 expands you'll see frame1 is not the full width. We need to make them sticky.

Make both frames sticky on NSEW.
Click RUN to see how the 2 frames are laid out in the GUI, and type text into the label until it expands.
Now, change frame2 to be in row 0, column 1 instead of row 1, column 0.
Click RUN to see how the 2 frames are laid out in the GUI now. Pretty cool!
TIPS
Frames make it much easier to lay out more complex GUI apps and to modify the layout if needed. We call code that is easy to change flexible
'''
from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("My GUI App")

# Create a frame for first 2 widgets
frame1 = Frame(root, bg="red")
frame1.grid(row=0, column=0, sticky="NSEW")

# Create a label and add it to the window using pack()
label1 = ttk.Label(frame1, text="My GUI App!")
label1.grid(row=0, column=0, padx=10, pady=5)

# Create a StringVar() to store text
words = StringVar()

# Create a text entry field
words_entry = ttk.Entry(frame1, textvariable=words)
words_entry.grid(row=1, column=0, padx=10, pady=5)

# Create a frame for the second 2 widgets
frame2 = Frame(root, bg="blue")
frame2.grid(row=0, column=1, sticky="NSEW")

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

'''LESSON 7.3
LEARN
Using a LabelFrame
Tkinter and ttk also offer us the LabelFrame widget. A LabelFrame is exactly what it sounds like - a frame with a label. We can pass in an optional text argument to put a label on the frame. It also puts a border around it automatically:
my_labelframe = ttk.LabelFrame(root, text="My Label Frame")
my_label = ttk.Label(my_labelframe, text="I am in the labelframe!")
Now that we have most of the widgets we need in our goal tracking app, let's use some labelframes to improve the layout even more.

Our widgets could be divided into two groups: ones that display things to the user and ones that the user interacts with, so let's group them that way.

CREATE
Complete the following tasks under the relevant comments

Create a LabelFrame called top_frame with the text Account Details and root as a parent.
Place the label frame at row 0, column 0 and give it 10px padding on all sides.
Make top_frame sticky in all 4 directions.
Change the parent for message_label, image_label and details_label to top_frame
Click RUN to see the updated GUI.
TIPS
Hmm... It doesn't quite look right, but that's because our other widgets are not in a frame, and so the ones in the second column have moved all the way over into a second column.

'''


from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
root.title("My GUI App")

# Create a frame for first 2 widgets
frame1 = Frame(root, bg="red")
frame1.grid(row=0, column=0, sticky = "NSEW")

# Create a label and add it to the window using pack()
label1 = ttk.Label(frame1, text="My GUI App!")
label1.grid(row=0, column=0, padx=10, pady=5)

#Create a StringVar() to store text
words = StringVar()

# Create a text entry field
words_entry = ttk.Entry(frame1, textvariable=words)
words_entry.grid(row=1, column=0, padx=10, pady=5)

# Create a frame for the second 2 widgets
frame2 = Frame(root, bg="blue")
frame2.grid(row=0, column=1,sticky="NSEW")

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
