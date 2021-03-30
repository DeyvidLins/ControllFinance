import sqlite3
import pyrebase
from PyQt5 import QtCore, QtGui, QtWidgets

conn = sqlite3.connect('Financeiro.db')
cur = conn.cursor()


#String/Dicionário de Conexão com o Firebase
firebaseConfig = {
    "apiKey": "AIzaSyAH61Y2Jb-1sbc1a2WvhaDELuE7FnefHKk",
    "authDomain": "controllfinance-44ace.firebaseapp.com",
    "databaseURL": "https://controllfinance-44ace-default-rtdb.firebaseio.com",
    "projectId": "controllfinance-44ace",
    "storageBucket": "controllfinance-44ace.appspot.com",
    "messagingSenderId": "11399726819",
    "appId": "1:11399726819:web:90d2d1b80a44d8509427d6",
    "measurementId": "G-LBGD17T06B"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
bd = firebase.database()


def create_sql(): # Funcao CRIAR
    cur.execute('''CREATE TABLE financa(id INTEGER PRIMARY KEY AUTOINCREMENT, desc VARCHAR(100) NOT NULL, 
               valor FLOAT NOT NULL,  dataVenc VARCHAR(15) NOT NULL,  dataPag varchar(15) NOT NULL, valorPag FLOAT NOT NULL,
               devendo  FLOAT NOT NULL, status varchar(2));''')
    conn.commit()



verify = cur.execute("SELECT name FROM sqlite_master where name ='financa' ")

verify = cur.fetchone()

# Se a Tabela não for Criada no banco, executar a função create_sql()
if verify is None:
    create_sql()

class ConectionForm():
    # Função para inserir dados no Sqllite
    def inserir (self,desc = '', valor = '', dataVenc = '', dataPag = '', valorPag = '', devendo = '', status = ''):

        self.desc = desc
        self.valor = valor
        self.dataVenc = dataVenc
        self.dataPag = dataPag
        self.valorPag = valorPag
        self.devendo = devendo
        self.status = status

        cur.execute(f'''INSERT INTO financa (desc,valor,dataVenc,dataPag,valorPag,devendo,status) 
                                                           VALUES ('{self.desc}','{self.valor}','{self.dataVenc}','{self.dataPag}',
                                                           '{self.valorPag}', '{self.devendo}', '{self.status}');''')

        conn.commit()
        conn.close()


    # Função para listar dados no Sqllite
    def banco_dados(self, table):

        # Retorna uma lista do sql
        conn = sqlite3.connect('Financeiro.db')
        cur = conn.cursor()
        cur.execute("select * from financa")
        c = cur.fetchall()
        table.setRowCount(len(c))
        table.setColumnCount(8)

        for i in range(0, len(c)):
            for j in range(0, 8):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))

        conn.commit()
        conn.close()


