from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' #donde estara nuestra base de datos
app.config['MYSQL_USER'] = 'root'       #usuario que usa para conectarse
app.config['MYSQL_PASSWORD'] = 'Iloveforyou'    #contraseña del usuario
app.config['MYSQL_DB'] = 'flasklogin'        #a que base de datos se conectara
mysql = MySQL(app)                      #para pasar la config a mi base de datos

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    data = cur.fetchall()
    cur.close()
    return render_template('login2.html', contacts = data) #a donde redigira con el nombre del archivo

# starting the app
if __name__ == '__main__':
    app.run(debug=True, port=8080) # lunch server