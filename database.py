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
    return products



def fetch_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales



# querry inserting a product
def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('milk',50,60,100);")
    conn.commit() # saving operations

# a querri inserting sales
def insert_sales():
    cur.execute(f"insert into sales(pid,quantity,created_at)values(20,7.01,'{current_datetime}');")
    conn.commit()

# insert_products()
# insert_sales()

# fetch_products()
# fetch_sales()

# TASK; modify your fetch and insert functions to be able to fetch and insert data from any table
# hint let your function take parameters eg.(table,data)
def fetch_products():
    cur.execute('select * from products;')
    products = cur.fetchall()
    return products
# fetch sales
def fetch_sales():
    cur.execute('select * from sales;')
    sales= cur.fetchall()
    return sales
# a function to fetch data from any table of your choice
def fetch_data(table):
    cur.execute(f"select * from {table};")
    data = cur.fetchall()
    return data
products = fetch_data('products')
sales = fetch_data('sales')
print(products)
print(sales)
# inserting data
# method 1-insert products function thata takes values as a parameter and uses placeholders(%S)
# no. of placeholders to mathc the no of values
def insert_products(values):
    insert = "insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit()

product1 =("laptop",30000,40000,10)
insert_products(product1)
products=fetch_data('products')
print(products)

# method2 insert data in any table
# this func takes table,columns,and values as parameters-uses f-string
# def insert_data(table,culumns,values):
#     cur.execute(f"insert into {table} {columns}  values{values}")
#     conn.commit()

# table ='products'
# columns ='name,buying_price,selling_price,stock_quantity'
# values =("bag,300,450,5")
# insert_data(table,columns,values)
# products = fetch_data('products')
# print(products)





