# IMPORT flask to use it
from flask import Flask, render_template

# initialise your application- initialization
app = Flask(__name__)

# __name__ special built in variable
# represents the name of the current file where your application is
# tells flask where your project starts
# parameters we can pass in a route function
# 1.Rule -eg //products,/sales,/users -defines the path a user accesses in the browser
 
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/products')
def products():
    return "My products page"
@app.route('/sales')
def sales():
    return "My sale page"

app.run(debug=True)