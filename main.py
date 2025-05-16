# IMPORT flask to use it
from flask import Flask, render_template,request,redirect,url_for,flash,session
from database import fetch_products , fetch_sales, insert_products,insert_sales,profit_per_product,sales_per_product,check_user,insert_user,insert_stock,fetch_stock,available_stock
from flask_bcrypt import Bcrypt
from functools import wraps
# initialise your application- initialization
app = Flask(__name__)

app.secret_key = '1234ab'

# initialize Bcrypt
bcrypt = Bcrypt(app) 



# __name__ special built in variable
# represents the name of the current file where your application is
# tells flask where your project starts
# parameters we can pass in a route function
# 1.Rule -eg //products,/sales,/users -defines the path a user accesses in the browser
 
@app.route('/')
def home():
    numbers = [1,2,3,4,5]
    return render_template("index.html",numbers=numbers)

def login_required(f):
    @wraps(f)
    def protected(*args,**kwrags):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwrags)
    return (protected)

@app.route('/test')
def test():
    flash('Testing flash messages','danger')
    return render_template("sample.html")

@app.route('/products')
@login_required
def products():
    products=fetch_products()
    return render_template("products.html", products=products)

@app.route('/add_products', methods=["GET","POST"])
def add_products():
    product_name = request.form['p-name']
    buying_price = request.form['b-price']
    selling_price = request.form['s-price']
    new_product = (product_name,buying_price,selling_price)
    insert_products(new_product)
    return redirect(url_for('products'))

@app.route('/sales')
@login_required
def sales():
    sales=fetch_sales()
    products=fetch_products()
    return render_template("sales.html" , sales=sales,products=products)

@app.route('/make_sale', methods=["GET","POST"])
def make_sale():
    product_id = request.form['pid']
    quantity = request.form['quantity']
    new_sale = (product_id,quantity)
    stock_available = available_stock(product_id)
    if stock_available < float(quantity):
        flash("Insufficient Stock","info")
    insert_sales(new_sale)
    flash("Sale made Successfully","Success")
    return redirect(url_for('sales'))





# TASK; 1. Create another list n annother route and loop through it using jinja to pass list values in a htmlpage

@app.route('/dashboard')
@login_required
def dashboard():
    
    profit_product = profit_per_product()
    sales_product = sales_per_product()

    product_name = [i[0] for i in profit_product]
    p_product = [float(i[1]) for i in profit_product]
    s_product = [float(i[1]) for i in sales_product]

    
    return render_template("dashboard.html" ,product_name=product_name,p_product=p_product,s_product=s_product)


@app.route('/register',methods =['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = check_user(email)
        print('registered')
        if not user :
            new_user = (name,email,phone_number,hashed_password)
            insert_user(new_user)
            return redirect(url_for('login'))
        else:
            print('Already registered')


    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = check_user(email)
        if not user:
            flash('user not found,please register','danger')
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(user[-1],password):
                flash('Logged in','success')
                session['email'] = email
                return redirect(url_for('dashboard'))
            else:
                flash('Incorect password','danger')

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('email',None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


@app.route('/stock')
def stock():
    # get products
    products = fetch_products()
    stock = fetch_stock()
    return render_template('stock.html',products=products,stock=stock)

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        product_id = request.form['pid']
        stock_quantity = request.form['quantity']
        new_stock = (product_id,stock_quantity)  
        insert_stock(new_stock)
        flash("stock added successfully", 'success')
        return redirect(url_for('stock'))  


app.run(debug=True)