'''Using rowspan and columnspan
Sometimes when we're using a grid layout system, we might want a widget to span over more than one row or column like so:



To do this, we can specify a columnspan or rowspan inside the .grid() function. A columnspan of 3 means that widget should take up 3 columns.

Another parameter we can set for widgets using the grid function is sticky. This makes the widget stick to specified edges of its container. To set sticky you pass in any combination of the letters N, S, W, E (compass directions) as either a string: sticky="NS" or a tuple: sticky=(N, NW)

Using sticky="WE" will make a widget the full width it can be, and sticky="NS" will make it full height. "NSWE" will make it fill all the space available to it.

CREATE
We've modified the code slightly so that you can explore columnspan and rowspan.

Edit the code to make button4 span 3 columns.
Make button5 span 2 rows.
Make button8 span 2 columns.
Click RUN to see how this looks. Hmm...
button4 should fill the width of the window, add a sticky parameter to make it do that.
Do the same for button8.
Lastly, button5 should fill the height of the space it is in, add a sticky parameter to do that.
'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Grid Test")

button1 = ttk.Button(root, text="Row 0, Col 0")
button1.grid(row=0, column=0)

button2 = ttk.Button(root, text="Row 0, Col 1")
button2.grid(row=0, column=1)

button3 = ttk.Button(root, text="Row 0, Col 2")
button3.grid(row=0, column=2)

button4 = ttk.Button(root, text="Row 1, Col 0")
button4.grid(row=1, column=0, columnspan=3, sticky="WE")

button5 = ttk.Button(root, text="Row 2, Col 0")
button5.grid(row=2, column=0, rowspan=2, sticky="NS")

button6 = ttk.Button(root, text="Row 2, Col 1")
button6.grid(row=2, column=1)

button7 = ttk.Button(root, text="Row 2, Col 2")
button7.grid(row=2, column=2)

button8 = ttk.Button(root, text="Row 3, Col 1")
button8.grid(row=3, column=1, columnspan=2, sticky="WE")

root.mainloop()
