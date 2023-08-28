from tkinter import *

tkRoot = Tk()
entries = []

# Form fields
def getFormInputs():
    global entries
    fields = ('Name', 'Gender', 'City', 'Age')
    rowCount = 0
    for f in fields:
        l = Label(tkRoot, text=f)
        e = Entry(tkRoot)

        l.grid(row=rowCount, column=1)
        e.grid(row=rowCount, column=2, sticky='ew')
        entries.append((f, e))
        
        rowCount += 1
    
    # Form buttons
    submitButton = Button(tkRoot, text='Show details', command=lambda:showDetails())
    submitButton.grid(row=len(fields)+1, columnspan=3, sticky='ew')

def showDetails():
    global entries
    r = len(entries) + 2
    for field in entries:
        fname = field[0]
        value = field[1].get()
        
        l1 = Label(tkRoot, text=fname)
        l2 = Label(tkRoot, text=value)
        
        l1.grid(row=r, column=1)
        l2.grid(row=r, column=2, sticky='ew')
        
        r += 1

getFormInputs()
tkRoot.mainloop()
