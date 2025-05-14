import psycopg2
from datetime import datetime

# create connection to db
conn = psycopg2.connect(user="postgres",password="123456789",host="localhost",port="5432",database="my_duka")

cur = conn.cursor()
current_datetime = datetime.now()
# func to fetch products
def fetch_products():
    cur.execute("select * from products;")

    products = cur.fetchall()
    return products



def fetch_sales():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock



# querry inserting a product

def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('milk',50,60,100);")
    conn.commit() # saving operations

# a querri inserting sales
# def insert_sales():
#     cur.execute(f"insert into sales(pid,quantity,created_at)values(20,7.01,'{current_datetime}');")
#     conn.commit()
def insert_sales(values):
    insert = "insert into sales(pid,quantity,created_at)values(%s,%s,'now()')"
    cur.execute(insert,values)
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

def insert_products(values):
    insert = "insert into products(name,buying_price,selling_price)values(%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit()



# print(products)

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


# profit per product
def profit_per_product():
    cur.execute("""select products.name, sum((products.selling_price -products.buying_price)*sales.quantity) as profit from products join sales on products.id = sales.pid group by(products.name);
                """)
    profit_per_product = cur.fetchall()
    return profit_per_product

# profit per day
def profit_per_day():
    cur.execute("""select date(sales.created_at) as date, sum((products.selling_price -products.buying_price)*sales.quantity) as profit from products join sales on products.id = sales.pid group by date;
                """)
    profit_per_day = cur.fetchall()
    return profit_per_day

# sales per product
def sales_per_product():
    cur.execute("""select products.name, sum(products.selling_price * sales.quantity) as revenue from products join sales on products.id = sales.pid group by(products.name);
                """)
    sales_per_product = cur.fetchall()
    return sales_per_product

# sales per day
def sales_per_day():
    cur.execute("""select date(sales.created_at) as date, sum(products.selling_price * sales.quantity) as revenue from sales join products on products.id = sales.pid group by date;
                """)
    sales_per_day = cur.fetchall()
    return sales_per_day



def check_user(email):
    query = "select * from users where email = %s"
    cur.execute(query,(email,))
    user = cur.fetchone()
    return user

def insert_user(user_details):
    query = "insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)"
    cur.execute(query,user_details)
    conn.commit()
    
    




    







