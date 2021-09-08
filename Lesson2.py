'''So far, when we import modules, we have done it like this:
import random

When we do it this way, we then have to use dot notation, or write the name of the module in front, to use the functions from the module, for example:
number = random.randint(1, 10)

Because we will use a lot of functions to write our GUI code, we're going to use a slightly different import syntax to make it easier. It looks like this:
from random import *

The import * means import all and it means we don't need to write random. before the functions and can generate a random number using:
number = randint(1,10)


Ok, so let's start at the beginning now. The first thing we need to do to use tkinter to create a GUI is import the module:

from tkinter import *
This is slightly different to our usual import syntax–click here for an explanation.

We can then use it to create a window by doing the following:

root = Tk()
The variable root can be any name, but root is used most often. To give the window a title, we use the following line:

root.title("Here is a window!")
And to get the window to run we use the mainloop() function, which goes at the end after all of your GUI code:

root.mainloop()
'''

from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Run the main window loop
root.mainloop()