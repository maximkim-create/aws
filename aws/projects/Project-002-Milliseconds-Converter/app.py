from flask import Flask, render_template, request
app = Flask(__name__)


def convert_milliseconds(milliseconds):
     seconds=(milliseconds/1000)%60
     minutes=(milliseconds/(1000*60))%60
     hours=(milliseconds/(1000*60*60))%24

     return seconds, minutes, hours
@app.route('/', methods=['POST','GET'])
def type_post():
     if request.method == 'POST':
          timepiece = request.form['number']
          if not timepiece.isnumeric():
               return render_template('index.html', not_valid = True, developer_name='Maxim')
          number = int(timepiece)
          if not 0 < number:
               return render_template('index.html', not_valid = True,developer_name='Maxim')
          return render_template('result.html',developer_name='Maxim', number= number, result = convert_milliseconds(number))


     else:
          return render_template('index.html',not_valid=False, developer_name='Maxim')






if __name__=='__main__':
     app.run(debug=True)
     #app.run(host='0.0.0.0', port=80)