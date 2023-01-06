from flask_mysqldb import MySQL
class Model:
    def __init__(self, app):
        self.mysql=MySQL(app)
        pass
        
    def existencia(self,cui,password):
        usuario={'cui':cui, 'password':password}
        query = "SELECT * FROM user WHERE cui=%(cui)s and password=%(password)s"
        cur=self.mysql.connection.cursor()
        cur.execute(query, usuario)
        data=cur.fetchall()
        if not data:
            return False
        else:
            return True

    def horariosemes(self,d):
        cur=self.mysql.connection.cursor()
        cur.execute('TRUNCATE TABLE horarios')
        self.mysql.connection.commit()
        cur.execute('INSERT INTO horarios SELECT * FROM horarios{}'.format(d))
        self.mysql.connection.commit()
    
    def actualizar(self):
        cur=self.mysql.connection.cursor()
        cur.execute("SELECT * FROM horarios")
        data = []
        contenido = {}
        resultados=cur.fetchall()
        for resultado in resultados:
            contenido={'id':resultado[0],'curso':resultado[1], 'dia':resultado[2], 'hora_inicio':resultado[3], 
                    'hora_final':resultado[4], 'profesor':resultado[5], 'grupo':resultado[6]}
            data.append(contenido)
        contenido={}
        return data
        
    def añadir(self,request):
        contenido={'curso':request.form['curso'], 'dia':request.form['dia'], 'hora_inicio':request.form['hora_inicio'], 
                    'hora_final':request.form['hora_final'], 'profesor':request.form['profesor'], 'grupo':request.form['grupo']}
        query="INSERT INTO horarios(curso,dia,hora_inicio,hora_final,profesor,grupo) VALUES(%(curso)s,%(dia)s,%(hora_inicio)s,%(hora_final)s,%(profesor)s,%(grupo)s)"
        cur=self.mysql.connection.cursor()
        cur.execute(query, contenido)
        self.mysql.connection.commit()#aqui ejecutamos la consulta
        
    def eliminar(self,id):
        cur=self.mysql.connection.cursor()
        cur.execute('DELETE FROM horarios WHERE id={}'.format(id))#el format nos sirve para poder remplazar en la instruccion sql el id
        self.mysql.connection.commit()#se ejecuto la consulta

    def examinar(self,horas):
        horas['curso']
