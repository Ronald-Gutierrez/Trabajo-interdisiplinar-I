from flask import Flask
from flask import request

app = Flask(__name__) # instancia

@app.route('/')
def index() :
    return 'Hola mundo' # return string

if __name__ == '__main__':  
 app.run(debug=True, port=8080) # lunch server  