# TASK; 1. Create another list n annother route and loop through it using jinja to pass list values in a htmlpage


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def list():
    fruits = ['Banana','Orange','Apple','Pineapple','Dates','ma']
    return render_template("index.html" , fruits=fruits)


app.run(debug=True)