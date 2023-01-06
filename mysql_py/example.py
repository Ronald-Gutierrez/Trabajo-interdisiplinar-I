from flask import Flask
from flask import request
from flask import jsonify
from flaskext .mysql import MySQL
app = Flask(__name__)
mysql = MySQL()
app.config[ 'MYSQL_DATABASE_USER'] = 'root'
app.config[ 'MYSQL_DATABASE_PASSWORD'] = 'Iloveforyou'
app.config[ 'MYSQL_DATABASE_DB'] = 'my_first_bd'
app.config[ 'MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

if __name__ == "__main__":
 app.run(debug=True)

@app.route('/create_task', methods=['POST'])
def create_task():
    print (request.json)
    params = {
    ' title ' : request.json['title'],
    ' description' : request.json['description']
    }
    query = """ insert into task ( title , description)
    10 values (%( title )s, %(description)s)"""
    cursor.execute(query, params)
    conn.commit()
    content = {'id': cursor.lastrowid , 'title' : params['title' ],'description'
    : params['description']}
    return jsonify (content)