from flask import Flask, render_template, session, request, redirect, url_for,flash
from modelo import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hardware+10'
app.config['MYSQL_DB'] = 'flaskdb'

modelo=Model(app)

app.secret_key='mysecretkey'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/ingreso',methods=["GET","POST"])
def ingreso():
    if modelo.existencia(request.form['cui'],request.form['password']):
        return  redirect(url_for('semestre'))
    else:
        return "Error password and CUI not match"
                
@app.route('/semestre',methods = ['POST','GET'])#nos enviara algo cada vez que entremos a nuestra pagina principal para evitar el not Found
def semestre():
    return render_template('semes.html')

#@app.route('/logout', methods=["GET", "POST"])
#def logout():
#    session.clear()
#    return render_template("login.html")

@app.route('/Form1/<string:a>',methods = ['POST','GET'])#nos enviara algo cada vez que entremos a nuestra pagina principal para evitar el not Found
def Form1(a):
    modelo.horariosemes(a)
    return redirect(url_for('Form'))

@app.route('/Form',methods = ['GET'])#nos enviara algo cada vez que entremos a nuestra pagina principal para evitar el not Found
def Form():
    return render_template('horario.html',horarios=modelo.actualizar())#enviara esta imagen, renderizara el formulario
    #el horarios=data es para poder mandar al html las tuplas creadas

@app.route('/add_contact',methods=['POST'])
def add_contact():# empezaremos a guardar datos
    modelo.añadir(request)
    flash("Curso Agregado")
    return redirect(url_for('Form'))#nos redirecciona otra vez al html incial esto despues de hacer la consulta


@app.route('/delete/<string:id>', methods = ['POST','GET'])#el string id porque esa es la condicion que pusimos para poder hacer el delete en una fila
def delete_contact(id):
    #pasaremos el id por una consulta sql para eliminar este id
    modelo.eliminar(id)
    flash('Curso eliminado del horario')  
    return redirect(url_for('Form'))
"""
@app.route('/comprobacion', methods = ['POST','GET'])
def comprobacion():
    cur=mysql.connection.cursor()
    #cur.execute('TRUNCATE TABLE grafico')
    #mysql.connection.commit()
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['7:00'])
    data=cur.fetchall()
    d1=data
    print(d1)
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['7:50'])
    data=cur.fetchall()
    d2=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['8:50'])
    data=cur.fetchall()
    d3=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['9:40'])
    data=cur.fetchall()
    d4=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['10:40'])
    data=cur.fetchall()
    d5=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['11:30'])
    data=cur.fetchall()
    d6=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['12:20'])
    data=cur.fetchall()
    d7=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['13:10'])
    data=cur.fetchall()
    d8=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['14:50'])
    data=cur.fetchall()
    d9=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['15:50'])
    data=cur.fetchall()
    d10=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['16:40'])
    data=cur.fetchall()
    d11=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['17:40'])
    data=cur.fetchall()
    d12=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['18:30'])
    data=cur.fetchall()
    d13=data
    cur.execute('SELECT * FROM horarios WHERE hora_inicio=%s',['19:30'])
    data=cur.fetchall()
    d14=data
    cur.close()
    tup = d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14
    dia = 'Lunes','Martes','Miercoles','Jueves','Viernes'
    hor = '07:00-07:50','07:50-08:40','08:50-09:40','09:40-10:30','10:40-11:30','11:30-12:20','12:20-13:10','13:10-14:00','14:50-15:40','15:50-16:40','16:40-17:30','17:40-18:30','18:30-19:20','19:30-20:20'
    return render_template('comprobacion.html',t=tup, h=hor, diad=dia)
"""
if __name__=='__main__':#si el archivo que se esta ejecutando es el main es decir el app.py entonces arranca el servidor
    app.run(port=3000,debug=True)#corre el servidor
