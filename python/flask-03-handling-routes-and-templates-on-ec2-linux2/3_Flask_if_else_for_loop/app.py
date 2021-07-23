#Import Flask modules
from flask import Flask, redirect, url_for, render_template
#Create an object named app 
app = Flask(__name__)
# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>' 
# and assign route of no path ('/')
@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'
# and assign to the static route of ('about')

# Create a function named error which returns a formatted string '<h1>Either you encountered an error or you are not authorized.</h1>' 
# and assign to the static route of ('error')
@app.route('/about')
def about():
    return '<h1> this is my about page </h1>'
# Create a function named hello which returns a string of '<h1>Hello, World! </h1>' 
# and assign to the static route of ('/hello')
@app.route('/error')
def error():
    return '<h1> either you encountered an error or unauthorized.</h1>'
# Create a function named admin which redirect the request to the error path 
# and assign to the route of ('/admin')

# Create a function named greet which return formatted inline html string 
# and assign to the dynamic route of ('/<name>')
@app.route('/hello')
def hello():
    return '<h1>hello,world!</h1>'
# Create a function named greet_admin which redirect the request to the hello path with param of 'Master Admin!!!!' 
# and assign to the route of ('/greet-admin')
@app.route('/admin')
def admin():
    return redirect(url_for('error'))
# Rewrite a function named greet which which uses template file named `greet.html` under `templates` folder 
# and assign to the dynamic route of ('/<name>')

 #Create a function named list10 which creates a list counting from 1 to 10 within `list10.html` 
# and assign to the route of ('/list10')
#@app.route('/<name>')
#def greet(name):
 
# Create a function named evens which show the even numbers from 1 to 10 within `evens.html` 
# and assign to the route of ('/evens')
@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name = 'Master Admin!!!!'))
@app.route('/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@app.route("/list10")
def list10():
    return render_template('list10.html')

@app.route("/evens")
def evens():
     return render_template('evens.html')




# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__=='__main__':
    app.run(debug=True)