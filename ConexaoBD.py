import sqlite3
import pyrebase


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

# Se a Tabela não foi Criado no banco ele executar a função create_sql()
if verify is None:
    create_sql()

class ConectionForm():
    def __init__(self,desc = '', valor = '', dataVenc = '', dataPag = '', valorPag = '', devendo = '', status = ''):

        self.desc = desc
        self.valor = valor
        self.dataVenc = dataVenc
        self.dataPag = dataPag
        self.valorPag = valorPag
        self.devendo = devendo
        self.status = status

    def __str__(self):

        cur.execute(f'''INSERT INTO financa (desc,valor,dataVenc,dataPag,valorPag,devendo,status) 
                                                   VALUES ('{self.desc}','{self.valor}','{self.dataVenc}','{self.dataPag}',
                                                   '{self.valorPag}', '{self.devendo}', '{self.status}');''')

        return conn.commit()
        conn.close()














