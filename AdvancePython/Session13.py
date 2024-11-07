from tkinter import *
from tkinter.font import * 


window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%dx%d'%(width,height))
window.state('zoomed')

window.grid_columnconfigure(0,weight=2)
window.grid_columnconfigure(1, weight=3)
window.grid_rowconfigure(0,weight=1)

window.title('نرم افزار مدیریت رستوران')

vazir_font = Font(family='Vazir', size=16)
pad_x = 5
pad_y = 5

######################################################################
bill_frame = LabelFrame(window, text='صورتحساب', bg='lavender', font=vazir_font, padx=pad_x , pady=pad_y)
bill_frame.grid(row=0, column=0 , sticky='nsew', padx=pad_x , pady=pad_y)

bill_frame.grid_columnconfigure(0, weight=1)
bill_frame.grid_rowconfigure(1, weight=1)

entry_order = Entry(bill_frame, font=vazir_font, width=15, justify='center')
entry_order.grid(row=0, column=0)

listbox_item = Listbox(bill_frame)
listbox_item.grid(row=1, column=0 , sticky='nsew', padx=pad_x , pady=pad_y)

listbox_button_frame = LabelFrame(bill_frame, bg='darkblue')
listbox_button_frame.grid(row=2, column=0 , sticky='nsew', padx=pad_x , pady=pad_y)

listbox_button_frame.grid_columnconfigure(0,weight=1)
listbox_button_frame.grid_columnconfigure(1,weight=1)
listbox_button_frame.grid_columnconfigure(2,weight=1)
listbox_button_frame.grid_columnconfigure(3,weight=1)


button_delete = Button(listbox_button_frame, text='حذف',font=vazir_font)
button_delete.grid(row=0 , column=0 ,sticky='nsew', padx=pad_x , pady=pad_y) 

button_new = Button(listbox_button_frame, text='فاکتور جدید',font=vazir_font)
button_new.grid(row=0 , column=1 ,sticky='nsew', padx=pad_x , pady=pad_y) 

button_add = Button(listbox_button_frame, text='+',font=vazir_font)
button_add.grid(row=0 , column=2 ,sticky='nsew', padx=pad_x , pady=pad_y) 

button_mines = Button(listbox_button_frame, text='-',font=vazir_font)
button_mines.grid(row=0 , column=3 ,sticky='nsew', padx=pad_x , pady=pad_y) 
######################################################################
menu_frame = LabelFrame(window, text='منو غذا و نوشیدنی', bg='lightblue', font=vazir_font, padx=pad_x , pady=pad_y)
menu_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x , pady=pad_y)

menu_frame.grid_columnconfigure(0,weight=1)
menu_frame.grid_columnconfigure(1,weight=2)

menu_frame.grid_rowconfigure(0,weight=1)

drink_frame = LabelFrame(menu_frame, text="نوشیدنی ها",font=vazir_font, padx=pad_x , pady=pad_y)
drink_frame.grid(row=0, column=0, sticky='nsew', padx=pad_x , pady=pad_y)

food_frame = LabelFrame(menu_frame, text="غذاها",font=vazir_font, padx=pad_x , pady=pad_y)
food_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x , pady=pad_y)

######################################################################
buttons_frame = LabelFrame(window,bg='darkblue', font=vazir_font, padx=pad_x , pady=pad_y)
buttons_frame.grid(row=1, column=1, padx=pad_x , pady=pad_y)

buttons_exit = Button(buttons_frame, text='خروج', font=vazir_font)
buttons_exit.grid(row=0 , column=0)

buttons_calculate = Button(buttons_frame, text='ماشین حساب', font=vazir_font)
buttons_calculate.grid(row=0 , column=1)

window.mainloop()
