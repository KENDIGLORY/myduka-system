# IMPORT flask to use it
from flask import Flask, render_template,request,redirect,url_for
from database import fetch_products , fetch_sales, insert_products

# initialise your application- initialization
app = Flask(__name__)

# __name__ special built in variable
# represents the name of the current file where your application is
# tells flask where your project starts
# parameters we can pass in a route function
# 1.Rule -eg //products,/sales,/users -defines the path a user accesses in the browser
 
@app.route('/home')
def home():
    numbers = [1,2,3,4,5]
    return render_template("index.html",numbers=numbers)

@app.route('/products')
def products():
    products=fetch_products()
    return render_template("products.html", products=products)

@app.route('/add_products', methods=["GET","POST"])
def add_products():
    product_name = request.form['p-name']
    buying_price = request.form['b-price']
    selling_price = request.form['s-price']
    stock_quantity = request.form['s-quantity']
    new_product = (product_name,buying_price,selling_price,stock_quantity)
    insert_products(new_product)
    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales=fetch_sales()
    return render_template("sales.html" , sales=sales)




# TASK; 1. Create another list n annother route and loop through it using jinja to pass list values in a htmlpage

@app.route('/')
def list():
    fruits = ['Banana','Orange','Apple','Pineapple','Dates']
    return render_template("index.html" , fruits=fruits)

# task 2. go and create tables using borrowed css(boostrap) -use boostrap to create tables with random data 

app.run(debug=True)