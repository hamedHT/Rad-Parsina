from tkinter import *
from tkinter.font import Font
import os
import sqlite3

# ---------------------- دیتابیس ----------------------
class Database:
    def __init__(self, db):
        self.db = db
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()

        # جدول منو (اصلاح نام جدول و اصلاح دستورات)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                ID INTEGER PRIMARY KEY UNIQUE NOT NULL,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                is_food INTEGER NOT NULL
            ) WITHOUT ROWID;
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER NOT NULL,
                food_id INTEGER NOT NULL,
                count INTEGER,
                price INTEGER,
                FOREIGN KEY(food_id) REFERENCES menu(ID)
            );
        """)
        self.connection.commit()

    def insert(self, id, name, price, is_food):
        try:
            self.cursor.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", (id, name, price, is_food))
            self.connection.commit()
        except sqlite3.IntegrityError:
            pass  # جلوگیری از تکرار در صورت وجود

    def get_menu_item(self, is_food):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        return self.cursor.execute("SELECT * FROM menu WHERE is_food = ?", (is_food,)).fetchall()

    def get_max_order_id(self):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        result = self.cursor.execute("SELECT MAX(order_id) FROM orders").fetchone()
        return result[0] if result and result[0] else 0

    def get_menu_item_by_name(self, name):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        return self.cursor.execute("SELECT * FROM menu WHERE name = ?", (name,)).fetchall()

    def insert_into_order(self, order_id, food_id, count, price):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO orders VALUES (?, ?, ?, ?)", (order_id, food_id, count, price))
        self.connection.commit()

    def get_order_item(self, order_id, food_id):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        return self.cursor.execute("SELECT * FROM orders WHERE order_id = ? AND food_id = ?",
                                   (order_id, food_id)).fetchall()

    def increase_count(self, order_id, food_id):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            UPDATE orders 
            SET count = count + 1 
            WHERE order_id = ? AND food_id = ?
        """, (order_id, food_id))
        self.connection.commit()

    def decrease_count(self, order_id, food_id):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            UPDATE orders 
            SET count = count - 1 
            WHERE order_id = ? AND food_id = ? AND count > 0
        """, (order_id, food_id))
        self.connection.commit()

    def delete_order_item(self, order_id, food_id):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM orders WHERE order_id = ? AND food_id = ?",
                            (order_id, food_id))
        self.connection.commit()

    def clear_order(self, order_id):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
        self.connection.commit()


# ---------------------- ایجاد دیتابیس و پر کردن اولیه ----------------------
db = None
if not os.path.isfile('restaurant.db'):
    db = Database('restaurant.db')
    db.insert(1, 'چلو مرغ', 80000, 1)
    db.insert(2, 'چلو کباب', 85000, 1)
    db.insert(3, 'چلو قیمه', 75000, 1)
    db.insert(4, 'نوشابه', 5000, 0)
    db.insert(5, 'دوغ', 4000, 0)
    db.insert(6, 'لیموناد', 6000, 0)
else:
    db = Database('restaurant.db')


# ---------------------- رابط کاربری ----------------------
window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width}x{height}')
window.state('zoomed')
window.title('نرم‌افزار مدیریت رستوران')

# تنظیمات فونت و استایل
vazir_font = Font(family='Vazir', size=14)
pad_x = 5
pad_y = 5

# ---------------------- فریم صورتحساب ----------------------
bill_frame = LabelFrame(window, text='صورتحساب', bg='lavender', font=vazir_font, padx=pad_x, pady=pad_y)
bill_frame.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)
bill_frame.grid_columnconfigure(0, weight=1)
bill_frame.grid_rowconfigure(1, weight=1)

# ورودی شماره سفارش
entry_order = Entry(bill_frame, font=vazir_font, width=15, justify='center')
entry_order.grid(row=0, column=0, pady=pad_y)

# پر کردن شماره سفارش فعلی
max_order_number = db.get_max_order_id() + 1
entry_order.insert(0, str(max_order_number))

# لیست‌باکس آیتم‌های سفارش
listbox_items = Listbox(bill_frame, font=vazir_font, justify='right', exportselection=False)
listbox_items.grid(row=1, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

# فریم دکمه‌های لیست‌باکس
listbox_button_frame = LabelFrame(bill_frame, bg='darkblue', font=vazir_font, padx=pad_x, pady=pad_y)
listbox_button_frame.grid(row=2, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

for i in range(4):
    listbox_button_frame.grid_columnconfigure(i, weight=1)

button_delete = Button(listbox_button_frame, text='حذف', font=vazir_font, command=lambda: delete_selected_item())
button_delete.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

button_new = Button(listbox_button_frame, text='فاکتور جدید', font=vazir_font, command=lambda: new_order())
button_new.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

button_add = Button(listbox_button_frame, text='+', font=vazir_font, command=lambda: increase_selected_item())
button_add.grid(row=0, column=2, sticky='nsew', padx=pad_x, pady=pad_y)

button_minus = Button(listbox_button_frame, text='-', font=vazir_font, command=lambda: decrease_selected_item())
button_minus.grid(row=0, column=3, sticky='nsew', padx=pad_x, pady=pad_y)

# ---------------------- فریم منو ----------------------
menu_frame = LabelFrame(window, text='منو غذا و نوشیدنی', bg='lightblue', font=vazir_font, padx=pad_x, pady=pad_y)
menu_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)
menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=1)
menu_frame.grid_rowconfigure(0, weight=1)

# فریم نوشیدنی‌ها
drink_frame = LabelFrame(menu_frame, text="نوشیدنی‌ها", font=vazir_font, padx=pad_x, pady=pad_y)
drink_frame.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)
drink_frame.grid_columnconfigure(0, weight=1)
drink_frame.grid_rowconfigure(0, weight=1)

listbox_drink = Listbox(drink_frame, font=vazir_font, exportselection=False, justify='right')
listbox_drink.grid(sticky='nsew')

drinks = db.get_menu_item(0)
for drink in drinks:
    listbox_drink.insert('end', drink[1])

# فریم غذاها
food_frame = LabelFrame(menu_frame, text="غذاها", font=vazir_font, padx=pad_x, pady=pad_y)
food_frame.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)
food_frame.grid_columnconfigure(0, weight=1)
food_frame.grid_rowconfigure(0, weight=1)

listbox_food = Listbox(food_frame, font=vazir_font, exportselection=False, justify='right')
listbox_food.grid(sticky='nsew')

foods = db.get_menu_item(1)
for food in foods:
    listbox_food.insert('end', food[1])

# ---------------------- توابع کاربردی ----------------------

def add_item_to_order(menu_name, is_food):
    order_id = entry_order.get()
    if not order_id:
        return
    try:
        order_id = int(order_id)
    except ValueError:
        return

    menu_item = db.get_menu_item_by_name(menu_name)
    if not menu_item:
        return

    menu_id = menu_item[0][0]
    price = menu_item[0][2]

    existing = db.get_order_item(order_id, menu_id)
    if not existing:
        db.insert_into_order(order_id, menu_id, 1, price)
    else:
        db.increase_count(order_id, menu_id)

    refresh_order_list(order_id)


# ---------------------- توابع کاربردی ----------------------
def refresh_order_list(order_id):
    listbox_items.delete(0, END)
    cursor = db.connection.cursor()
    cursor.execute("""
        SELECT m.name, o.count, m.price, (o.count * m.price) 
        FROM orders o 
        JOIN menu m ON o.food_id = m.ID 
        WHERE o.order_id = ?
    """, (order_id,))
    rows = cursor.fetchall()
    total = 0
    for row in rows:
        item_str = f"{row[0]}   x{row[1]}   {row[2]:,} تومان   =   {row[3]:,} تومان"
        listbox_items.insert(END, item_str)
        total += row[3]
    listbox_items.insert(END, "-" * 40)
    listbox_items.insert(END, f"مبلغ کل: {total:,} تومان")


def get_selected_item_name():
    selected = listbox_items.curselection()
    if not selected:
        return None
    line = listbox_items.get(selected[0])
    # فرمت: "نام   xتعداد   قیمت   =   مبلغ کل"
    # پس از split با "   x"، اولین بخش نام است
    if "x" in line:
        return line.split("   x")[0].strip()
    return None


def delete_selected_item():
    name = get_selected_item_name()
    if not name:
        return
    try:
        order_id = int(entry_order.get())
    except ValueError:
        return
    menu_item = db.get_menu_item_by_name(name)
    if menu_item:
        db.delete_order_item(order_id, menu_item[0][0])
        refresh_order_list(order_id)


def increase_selected_item():
    name = get_selected_item_name()
    if not name:
        return
    try:
        order_id = int(entry_order.get())
    except ValueError:
        return
    menu_item = db.get_menu_item_by_name(name)
    if menu_item:
        db.increase_count(order_id, menu_item[0][0])
        refresh_order_list(order_id)


def decrease_selected_item():
    name = get_selected_item_name()
    if not name:
        return
    try:
        order_id = int(entry_order.get())
    except ValueError:
        return
    menu_item = db.get_menu_item_by_name(name)
    if menu_item:
        db.decrease_count(order_id, menu_item[0][0])
        refresh_order_list(order_id)



def new_order():
    global max_order_number
    max_order_number = db.get_max_order_id() + 1
    entry_order.delete(0, END)
    entry_order.insert(0, str(max_order_number))
    listbox_items.delete(0, END)


# ---------------------- پیوند رویدادها ----------------------
def add_drink(event):
    selected = listbox_drink.curselection()
    if selected:
        drink_name = listbox_drink.get(selected[0])
        add_item_to_order(drink_name, False)


def add_food(event):
    selected = listbox_food.curselection()
    if selected:
        food_name = listbox_food.get(selected[0])
        add_item_to_order(food_name, True)


listbox_drink.bind('<Double-Button-1>', add_drink)
listbox_food.bind('<Double-Button-1>', add_food)

# ---------------------- فریم دکمه‌های پایین ----------------------
buttons_frame = LabelFrame(window, bg='darkblue', font=vazir_font, padx=pad_x, pady=pad_y)
buttons_frame.grid(row=1, column=1, sticky='nsew', padx=pad_x, pady=pad_y)
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)

button_exit = Button(buttons_frame, text='خروج', font=vazir_font, command=window.quit)
button_exit.grid(row=0, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

button_calculate = Button(buttons_frame, text='ماشین حساب', font=vazir_font,
                          command=lambda: os.system("calc"))  # اجرای ماشین‌حساب ویندوز
button_calculate.grid(row=0, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

# ---------------------- اجرای اولیه ----------------------
refresh_order_list(max_order_number)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=0)
window.grid_columnconfigure(0, weight=2)
window.grid_columnconfigure(1, weight=3)

window.mainloop()
