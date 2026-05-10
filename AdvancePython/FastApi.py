# main.py
from fastapi import FastAPI, HTTPException, Query, Path, Body, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import sqlite3
import os

# ---------------------- تنظیمات اولیه ----------------------
app = FastAPI(
    title="آموزش FastAPI — سیستم مدیریت محصولات",
    description="یک API ساده برای آموزش مفاهیم اصلی FastAPI",
    version="1.0.0"
)

# ---------------------- مدل داده (Pydantic) ----------------------
class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2, max_length=50, description="نام محصول")
    price: float = Field(..., gt=0, description="قیمت باید بزرگتر از ۰ باشد")
    category: str = Field(default="عمومی", description="دسته‌بندی محصول")

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('نام نمی‌تواند خالی باشد')
        return v.strip()


# ---------------------- اتصال به دیتابیس SQLite ----------------------
DB_PATH = "products.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

if not os.path.exists(DB_PATH):
    init_db()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------- مسیرهای اصلی (Endpoints) ----------------------

@app.get("/", tags=["General"])
def read_root():
    return {
        "message": "به API آموزشی خوش آمدید!",
        "docs": "/docs",
        "status": "online"
    }


#  دریافت لیست محصولات با فیلتر و مرتب‌سازی (Query Parameters)
@app.get("/products", response_model=List[Product], tags=["Products"])
def get_products(
    category: Optional[str] = Query(None, description="فیلتر بر اساس دسته‌بندی"),
    sort_by: str = Query("name", description="مرتب‌سازی بر اساس (name یا price)"),
    order: str = Query("asc", description="asc یا desc")
):
    conn = get_db()
    cursor = conn.cursor()
    
    query = "SELECT * FROM products"
    params = []

    if category:
        query += " WHERE category = ?"
        params.append(category)

    # اعتبارسنجی مرتب‌سازی
    if sort_by not in ["name", "price"]:
        sort_by = "name"
    if order not in ["asc", "desc"]:
        order = "asc"

    query += f" ORDER BY {sort_by} {order.upper()}"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    products = [Product(id=row["id"], name=row["name"], price=row["price"], category=row["category"]) for row in rows]
    return products


#  دریافت محصول توسط ID (Path Parameter)
@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product(
    product_id: int = Path(..., gt=0, description="شناسه محصول (باید عددی مثبت باشد)")
):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="محصول پیدا نشد")

    return Product(id=row["id"], name=row["name"], price=row["price"], category=row["category"])


#  ایجاد محصول جدید (Request Body)
@app.post("/products", status_code=status.HTTP_201_CREATED, tags=["Products"])
def create_product(product: Product = Body(...)):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
            (product.name, product.price, product.category)
        )
        conn.commit()
        product.id = cursor.lastrowid
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"خطا در پایگاه داده: {str(e)}")
    finally:
        conn.close()

    return {"message": "محصول با موفقیت اضافه شد", "product": product}


#  بروزرسانی محصول (PUT)
@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
def update_product(
    product_id: int = Path(..., gt=0),
    product: Product = Body(...)
):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="محصول پیدا نشد")

    cursor.execute(
        "UPDATE products SET name = ?, price = ?, category = ? WHERE id = ?",
        (product.name, product.price, product.category, product_id)
    )
    conn.commit()
    conn.close()

    return product


#  حذف محصول (DELETE)
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
def delete_product(product_id: int = Path(..., gt=0)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="محصول پیدا نشد")

    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    return None


# ---------------------- اجرای سرور ----------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
