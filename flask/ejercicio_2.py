from flask import Flask
from flask import request

app = Flask(__name__) # instancia

# params followed by slashes
@app.route('/method4/') # accept 0 params
@app.route('/method4/<int:num1>/') # one param
@app.route('/method4/<int:num1>/<int:num2>') # two params
@app.route('/method4/<int:num1>/<int:num2>/<int:num3>') # three params
def method4(num1='No num', num2='no num', num3='no num'):
    return 'El promedio es: ' + str((num1+num2+num3)/3)
if __name__ == '__main__':
    app.run(debug=True, port=8080) # lunch server