'''

Review GUI basics
Congratulations! You have made it to the last lesson in this course. We have covered the basics of GUI and OOP code and built a pretty robust application. This lesson will review what you have learned in this course.

A Graphical User Interface is all about giving your users a window with widgets that they can interact with. Let's recap some of what we learned about using Tkinter.

CREATE
Each of these tasks replaces a ??? in the code, although some may be more than 1 line of code.

Import tkinter and ttk at the start of the program.
Create a new window called root with the title Congratulations!
Create a StringVar() called name that will store the user's name.
Complete the code to create the image happy_image using /images/python/happy.png as the file.
Add an argument to the Entry widget code so that the name typed in there will be shown in name_label as the user types.
Click RUN and enter your name in the entry field to see your certificate!

'''
# Imports
from tkinter import *
from tkinter import ttk

# Create window
root = Tk()
root.title("Congratulations!")

# Add labels
congrats_label = ttk.Label(root, text="Congratulations to:")
congrats_label.grid(row=0, column=0)

# Variable for storing and displaying name
name = StringVar()
name.set("Please enter your name")

name_label = ttk.Label(root, textvariable=name)
name_label.grid(row=1, column=0)

course_label = ttk.Label(root, text="For completing the Code Avengers Level 3 Python Course!")
course_label.grid(row=2, column=0)

# Add happy image
happy_image = PhotoImage(file="snapchat.png")
image_label = ttk.Label(root, image=happy_image)
image_label.grid(row=3, column=0)

# Entry field for typing in name
name_entry = ttk.Entry(root, textvariable=name)
name_entry.grid(row=4, column=0)

# Add padding
for child in root.winfo_children():
    child.grid(padx=15, pady=10)

root.mainloop()
