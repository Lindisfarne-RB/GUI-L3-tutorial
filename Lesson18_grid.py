'''Introduction to the .grid() layout system
Our GUI for our goal tracking app is starting to get a bit more complex now that we have added so many widgets. It would be nice if we could have some more control over how they are placed in the window.

We have been using .pack() to place the widgets in the window, but tkinter also has another geometry manager called .grid().

With .grid() you set which row and column you want the widget to appear in, and it goes there:
my_button = ttk.Button(root, test="Click Me!")
my_button.grid(row=0, column=0)
(0, 0) is the top left corner of the window. Nice and easy, as long as you plan your grid well and use it for all of your widgets. Let's test it out first.

CREATE
In the editor is a window with 9 buttons. Each button is labeled with the row and column it should be in, but .pack() has been used.

Change .pack() to .grid() and put each button in the correct row and column.
Click RUN to check you have got an accurate 3x3 grid!
TIPS
As you can see, with .grid(), it doesn't matter what order you create the widgets in as long as you get the rows and columns accurate for where you want them.

'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Grid Test")

button1 = ttk.Button(root, text="Row 0, Col 0")
button1.grid(row=0, column=0)

button2 = ttk.Button(root, text="Row 1, Col 2")
button2.grid(row=1, column=2)

button3 = ttk.Button(root, text="Row 2, Col 2")
button3.grid(row=2, column=2)

button4 = ttk.Button(root, text="Row 1, Col 0")
button4.grid(row=1, column=0)

button5 = ttk.Button(root, text="Row 0, Col 1")
button5.grid(row=0, column=1)

button6 = ttk.Button(root, text="Row 0, Col 2")
button6.grid(row=0, column=2)

button7 = ttk.Button(root, text="Row 1, Col 1")
button7.grid(row=1, column=1)

button8 = ttk.Button(root, text="Row 2, Col 1")
button8.grid(row=2, column=1)
button9 = ttk.Button(root, text="Row 2, Col 0")
button9.grid(row=2, column=0)

root.mainloop()
