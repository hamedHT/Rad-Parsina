from tkinter import *
from tkinter.font import *
from tkinter import messagebox

def calculate():
    unit_from = list_box_from.get(ACTIVE)
    unit_to = list_box_to.get(ACTIVE)
    value_from = int(entry_from.get())
    if unit_from == 'centimeter':
        if unit_to == 'centimeter':
            result = value_from
        if unit_to == 'meter':
            result = value_from/100
        elif unit_to == 'kilometer':   
            result = (value_from/100)/100
    messagebox.showinfo(title='Result',message=result)
    entry_to.delete(0,END)
    entry_to.insert(END,result) 


window = Tk()

my_font = Font(family='consolas', size=18)
pad_x = 5
pad_y = 5

label_from = Label(window,text='From',font= my_font)
label_to = Label(window,text='to',font= my_font)
label_from.grid(row=0, column=0, padx=pad_x, pady= pad_y)
label_to.grid(row=0, column=1, padx=pad_x, pady= pad_y)

entry_from = Entry(window,font= my_font, bg='yellow', fg='blue')
entry_to = Entry(window,font= my_font, bg='yellow', fg='blue')
entry_from.grid(row=1, column=0, padx=pad_x, pady= pad_y)
entry_to.grid(row=1, column=1, padx=pad_x, pady= pad_y)

list_box_from = Listbox(window,exportselection=False,font= my_font)
list_box_to = Listbox(window,exportselection=False,font= my_font)
list_box_from.grid(row=2, column=0)
list_box_to.grid(row=2, column=1)
list_box_from.insert(END, 'centimeter')
list_box_from.insert(END, 'meter')
list_box_from.insert(END, 'kilometer')
list_box_from.insert(END, 'mile')
list_box_from.insert(END, 'yard')
list_box_to.insert(END, 'centimeter')
list_box_to.insert(END, 'meter')
list_box_to.insert(END, 'kilometer')
list_box_to.insert(END, 'mile')
list_box_to.insert(END, 'yard')

button = Button(window, text="calculate",font= my_font, command=calculate)
button.grid(row=3, column=0, columnspan=2, sticky='W,E',padx=pad_x, pady= pad_y)

window.mainloop()