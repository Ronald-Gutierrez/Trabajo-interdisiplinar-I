from flask import Flask
from flask import request

app = Flask(__name__) # instancia

@app.route('/') #wrap (decorator)
def index() :
    return 'Hola mundo' # return string

# GET param
@app.route('/method1')
def method1():
    param = request.args.get('param1', 'without data')
    return 'the param is: ' + str (param)

if __name__ == '__main__':
     app.run(debug=True, port=8080) # lunch server

#enviar paramentros http://127.0.0.1:8080/method1?param1=Ronald