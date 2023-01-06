from flask import Flask
from flask import request

app = Flask(__name__) # instancia

# params followed by slashes
@app.route('/method3/') # accept 0 params
@app.route('/method3/<name>/') # one param
@app.route('/method3/<name>/<surname>') # two params
def method3(name='No data', surname='no surname'):
    return 'Hola ' + str (name) + ' '  + str (surname)
if __name__ == '__main__':
    app.run(debug=True, port=8080) # lunch server