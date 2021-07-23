from flask import Flask

app = Flask(__name__)
@app.route("/")
def head():
    return "Hello World!"

@app.route('/maxim')
def second():
    return "THis is the Maxim's page"
@app.route('/third/subthird')
def third():
    return "this is the subpage of third page"

@app.route("/fourth/<string:id>")
def fourth(id):
    return f'Id of this page is {id}'

if __name__=='__main__':
    app.run(debug = True)