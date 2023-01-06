from flask import Flask
from flask import request

app = Flask(__name__) # instancia

# params followed by slashes
@app.route('/method2/') # accept 0 params
@app.route('/method2/<name>/') # one param
@app.route('/method2/<name>/<int:dni>') # two params
def method2(name='No data', dni='no dni'):
    return 'the param is: ' + str (name) + ''  + str (dni)
if __name__ == '__main__':
    app.run(debug=True, port=8080) # lunch server