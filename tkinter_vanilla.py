import tkinter as tk
from tkinter import ttk
'''
These two lines tell Python that our program needs two modules. The first, "tkinter", is the standard binding to Tk,
which when loaded also causes the existing Tk library on your system to be loaded. The second, "ttk", is Python's binding
to the newer "themed widgets" that were added to Tk in 8.5.
'''

def calculate(*args):
    '''
    Here we define our calculate procedure, which is called either when the user presses the Calculate button, or hits
    the Return key. It performs the feet to meters calculation, taking the number of feet from our entry widget, and  
    placing the result in our label widget.

    Say what? It doesn't look like we're doing anything with those widgets! Here's where the magic "textvariable"
    options we specified when creating the widgets come into play. We specified the global variable "feet" as the
    textvariable for the entry, which means that anytime the entry changes, Tk will automatically update the global
    variable feet. Similarly, if we explicitly change the value of a textvariable associated with a widget (as we're
    doing for "meters" which is attached to our label), the widget will automatically be updated with the current
    contents of the variable. Slick.
    '''
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root = tk.Tk()
#test at top
root.title("Feet to Meters")
mainframe = ttk.Frame(root, padding="2 2 3 2")#frame widget: left padding, top padding, right padding, bottom padding
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
mainframe.columnconfigure(0, weight=1)#auto strech if needed
mainframe.rowconfigure(0, weight=1)#auto strech if needed

'''
Next, the above lines set up the main window, giving it the title "Feet to Meters". Next, we create a frame widget,
which will hold all the content of our user interface, and place that in our main window. The "columnconfigure"/"rowconfigure"
bits just tell Tk that if the main window is resized, the frame should expand to take up the extra space.
'''

#Instanciate instances of these classes 
feet = tk.StringVar()
meters = tk.StringVar()
print (feet, type(feet))

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)#widget 1
feet_entry.grid(column=2, row=1, sticky=('W', 'E'))#widget 1 placement parameters

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=('W', 'E'))#wiget 2 is where result is shown
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky='W')#widget 3?
'''
The preceding lines create the three main widgets in our program: the entry where we type the number of feet in, a
label where we put the resulting number of meters, and the calculate button that we press to perform the calculation.

For each of the three widgets, we need to do two things: create the widget itself, and then place it onscreen.
All three widgets, which are 'children' of our content window are created as instances of one of Tk's themed widget classes.
At the same time as we create them, we give them certain options, such as how wide the entry is, the text to put inside the
Button, etc. The entry and label each are assigned a mysterious "textvariable"; we'll see what that does shortly.

If the widgets are just created, they won't automatically show up on screen, because Tk doesn't know how you want them to be
placed relative to other widgets. That's what the "grid" part does. Remembering the layout grid for our application, we place
each widget in the appropriate column (1, 2 or 3), and row (also 1, 2 or 3). The "sticky" option says how the widget would line
up within the grid cell, using compass directions. So "w" (west) means anchor the widget to the left side of the cell, "we"
(west-east) means anchor it to both the left and right sides, and so on.
'''
#text in body
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky='W')
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky='E')
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky='W')

'''
The above three lines do exactly the same thing for the three static text labels in our user interface; create each one,
and place it onscreen in the appropriate cell in the grid.
'''

for child in mainframe.winfo_children():
   child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
