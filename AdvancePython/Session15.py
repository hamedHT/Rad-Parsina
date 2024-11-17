from tkinter import *
from tkinter.font import * 
import os

############################################################################ DB

import sqlite3

class Database():
    def __init__(self,db):
        self.__db = db
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
                                CREATE TABLE if not exists[menu](
                                [ID] INT PRIMARY KEY NOT NULL UNIQUE, 
                                [name] NVARCHAR(50) NOT NULL, 
                                [price] INT NOT NULL,
                                [is_food] bool not null) WITHOUT ROWID;
                                """)
        
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS [ORDER](
                            ORDER_ID INT NOT NULL,
                            FOOD_ID INT NOT NULL REFERENCES[MENU] ([ID]),
                            COUNT INT,
                            price int);
                            """)
        self.connection.commit()

    def insert(self, id, name, price, is_food):
        self.cursor.execute("insert into [menu] values (?,?,?,?)",(id, name, price,is_food))
        self.connection.commit()

    def get_menu_item(self, is_food):
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()
        return self.cursor.execute("select * from [menu] where is_food = ?",(is_food,))
    
    def get_max_order(self):
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("select max(order_id) from [order]")
        result = self.cursor.fetchall()
        return result
    
    def get_menu_item_byname(self,menu_item_name):
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("select * from [menu] where name = ?",(menu_item_name,))
        result = self.cursor.fetchall()
        return result

    def insert_into_order(self, order_id, menu_id, count, price):
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("insert into order values (?,?,?,?)",(order_id, menu_id, count, price))
        self.connection.commit()

    def get_order_by_orderid(self, order_id, menu_id):
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("select * from order where order_id = ? and menu_id = ?",(order_id, menu_id))
        result = self.cursor.fetchall()
        return result
    
    def increase_count(self, order_id, menu_id):
        self.connection = sqlite3.connect(self.__db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""update order set count = count+1 where order_id = ? and menu_id = ?
                            """,(order_id, menu_id))
        self.connection.commit()

db = None
if os.path.isfile('restaurant.db')== False:
    db = Database('restaurant.db')
    db.insert(1,'چلو مرغ',800000,True)
    db.insert(2,'چلو کباب',800000,True)    
    db.insert(3,'چلو قیمه',800000,True)    
    db.insert(4,' نوشابه',800000,False)    
    db.insert(5,' دوغ',800000,False)    
    db.insert(6,'لیموناد ',800000,False) 
else:
    db = Database('restaurant.db')   

############################################################################

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

max_order_number = db.get_max_order()
if max_order_number[0][0] == None:
    max_order_number = 1
else:
    max_order_number = int(max_order_number[0][0])
entry_order.insert(0,max_order_number)
max_order_number += 1

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

drink_frame.grid_columnconfigure(0,weight=1)
drink_frame.grid_rowconfigure(0,weight=1)
listbox_drink = Listbox(drink_frame, font=vazir_font, exportselection=False)
listbox_drink.grid(sticky='nsew')
listbox_drink.configure(justify='right')

drinks = db.get_menu_item(False)
for drink in drinks:
    listbox_drink.insert('end', drink[1])

def add_drink(event):
    drink_item = db.get_menu_item_byname(listbox_drink.get(ACTIVE))
    menu_id = drink_item[0][0]
    price = drink_item[0][2]
    order_id = entry_order.get()
    result = db.get_order_by_orderid(order_id,menu_id)
    if len(result) == 0:
        db.insert_into_order(order_id, menu_id, 1,price)
    else:
        db.increase_count(order_id,menu_id)
listbox_drink.bind('<Double-Button>',add_drink)

food_frame = LabelFrame(menu_frame, text="غذاها",font=vazir_font, padx=pad_x , pady=pad_y)
food_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x , pady=pad_y)

food_frame.grid_columnconfigure(0,weight=1)
food_frame.grid_rowconfigure(0,weight=1)
listbox_food = Listbox(food_frame, font=vazir_font,exportselection=False)
listbox_food.grid(sticky='nsew')
listbox_food.configure(justify='right')

foods = db.get_menu_item(True)
for food in foods:
    listbox_food.insert('end', food[1])

def add_food(event):
    food_item = db.get_menu_item_byname(listbox_food.get(ACTIVE))
    print(food_item)

listbox_food.bind('<Double-Button>',add_food)
######################################################################
buttons_frame = LabelFrame(window,bg='darkblue', font=vazir_font, padx=pad_x , pady=pad_y)
buttons_frame.grid(row=1, column=1, padx=pad_x , pady=pad_y)

buttons_exit = Button(buttons_frame, text='خروج', font=vazir_font)
buttons_exit.grid(row=0 , column=0)

buttons_calculate = Button(buttons_frame, text='ماشین حساب', font=vazir_font)
buttons_calculate.grid(row=0 , column=1)

window.mainloop()
