'''Putting an image in a label
We can also put images in labels! This is a handy way of getting any images you need into a GUI app.

To add an image, we do it in a similar way to how we used a variable. First we have to create a PhotoImage() variable with the name or path to the image stored in it:

happy_image =  PhotoImage(file="/images/python/happy.png")
Then, we set an image parameter on the label to the variable the image is stored in, and pack it into the GUI:
my_label = Label(root, image=happy_image)
my_label.pack()'''
'''CREATE
Under the relevant comment create a PhotoImage() variable called neutral_image storing the image /images/python/neutral.png.
Under the next comment, create a new label called image_label and set the image to our neutral image.
Pack the label into the GUI
Note: PNG images are only supported in tkinter 8.6+'''

from tkinter import *

root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create the message label and add it to the window using pack()
message_label = Label(root, textvariable=message_text, wraplength=250)
message_label.pack()

# Create a PhotoImage()
neutral_image = PhotoImage(file="neutral.png")

# Create a new Label using the PhotoImage and pack it into the GUI
image_label = Label(root, image=neutral_image)
image_label.pack()

# Run the main window loop
root.mainloop()