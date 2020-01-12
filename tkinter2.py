import tkinter as tk
from tkinter import ttk
#calculator
'''
These two lines tell Python that our program needs two modules. The first, "tkinter", is the standard binding to Tk,
which when loaded also causes the existing Tk library on your system to be loaded. The second, "ttk", is Python's binding
to the newer "themed widgets" that were added to Tk in 8.5.
'''

def calculate(*args):#needs args here or hitting enter breaks
    if function_entry.get() == '+':
        results.set(float(a.get()) + float(b.get()))
    if function_entry.get() == '-':
        results.set(float(a.get()) - float(b.get()))
    if function_entry.get() == '/' or function_entry.get() == '\\':
        results.set(float(a.get()) / float(b.get()))
    if function_entry.get() == '*':
        results.set(float(a.get()) * float(b.get()))
    
root = tk.Tk()
#instaniate tk
#test at top
root.title("Calc")
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
a = tk.StringVar()
b = tk.StringVar()
function = tk.StringVar()
results = tk.StringVar()

a_entry = ttk.Entry(mainframe, width=9, textvariable=a)#widget 1 val A
a_entry.grid(column=1, row=1, sticky=('W', 'E'))#widget 1 placement parameters

function_entry = ttk.Entry(mainframe, width=9, textvariable=function)#widget 2 func
function_entry.grid(column=1, row=2, sticky=('W', 'E'))#widget 2 placement parameters

b_entry = ttk.Entry(mainframe, width=9, textvariable=b)#widget 3 Val B
b_entry.grid(column=1, row=3, sticky=('W', 'E'))#widget 3 placement parameters



ttk.Label(mainframe, textvariable=results).grid(column=2, row=4, sticky=('W', 'E'))#wiget 4 is where result is shown
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=2, sticky='W')#widget 5

'''
The preceding lines create the three main widgets in our program: the entry where we type the number of feet in, a
label where we put the resulting number of meters, and the calculate button that we press to perform the calculation.
'''

#text in body
ttk.Label(mainframe, text="Value A").grid(column=2, row=1, sticky='W')
ttk.Label(mainframe, text="-/+/*//").grid(column=2, row=2, sticky='W')
ttk.Label(mainframe, text="Value B").grid(column=2, row=3, sticky='W')

ttk.Label(mainframe, text="Equals").grid(column=1, row=4, sticky='E')
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

'''
The above three lines do exactly the same thing for the three static text labels in our user interface; create each one,
and place it onscreen in the appropriate cell in the grid.
'''

for child in mainframe.winfo_children():#1
   child.grid_configure(padx=5, pady=5)
   '''
   adds a little bit of padding around each,  so they aren't so scrunched together. 
   '''

a_entry.focus()#2
'''
The second line tells Tk to put the focus on our entry widget. That way the cursor will start in that field, so the user doesn't have
to click in it before starting to type.
'''

root.bind('<Return>', calculate)

'''
The third line tells Tk that if the user presses the Return key (Enter on Windows) anywhere within the root window, that it should call
our calculate routine, the same as if the user pressed the Calculate button.
'''
root.mainloop()
