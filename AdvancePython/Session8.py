from tkinter import *

window = Tk()

label_from = Label(window,text='From')
label_to = Label(window,text='to')
label_from.grid(row=0, column=0)
label_to.grid(row=0, column=1)

entry_from = Entry(window)
entry_to = Entry(window)
entry_from.grid(row=1, column=0)
entry_to.grid(row=1, column=1)

list_box_from = Listbox(window)
list_box_to = Listbox(window)
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

button = Button(window, text="calculate")
button.grid(row=3, column=0, columnspan=2, sticky='W,E')

window.mainloop()