import psycopg2
from datetime import datetime

# create connection to db
conn = psycopg2.connect(user="postgres",password="123456789",host="localhost",port="5432",database="myduka")

cur = conn.cursor()
current_datetime = datetime.now()
# func to fetch products
def fetch_products():
    cur.execute("select * from products;")

    products = cur.fetchall()
    for product in products:

        print(product)


def fetch_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    for sale in sales:
        print(sale)

# fetch_products()
# fetch_sales()


# a querry inserting a product
def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('milk',50,60,100);")
    conn.commit() # saving operations

# a querri inserting sales
def insert_sales():
    cur.execute(f"insert into sales(pid,quantity,created_at)values(20,7.01,'{current_datetime}');")
    conn.commit()

insert_products()
insert_sales()

fetch_products()
fetch_sales()





