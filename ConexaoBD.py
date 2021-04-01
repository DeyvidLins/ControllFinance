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


class ConectionForm():
    # Função para Criar as tabelas no banco
    def create_sql(self):
        cur.execute('''CREATE TABLE financa(id INTEGER PRIMARY KEY AUTOINCREMENT, desc VARCHAR(100) NOT NULL, 
                   valor FLOAT NOT NULL,  dataVenc VARCHAR(15) NOT NULL,  dataPag varchar(15) NOT NULL, valorPag FLOAT NOT NULL,
                   devendo  FLOAT NOT NULL, status varchar(2));''')
        conn.commit()

    # Função para Inserir dados
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



    # Função para Listar dados
    def listar(self, table):

        # Retorna uma lista do sql
        conn = sqlite3.connect('Financeiro.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM financa")
        c = cur.fetchall()
        table.setRowCount(len(c))
        table.setColumnCount(8)

        for i in range(0, len(c)):
            for j in range(0, 8):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))

        conn.commit()


    # Função para Excluir dados
    def excluir(self, linha):
        cur.execute("SELECT id FROM financa")
        c = cur.fetchall()
        id = c[linha][0]
        cur.execute(f"delete from financa where id = {id}")


        conn.commit()


    # Função para Atualizar dados
    def atualizar(self, id = '', desc = '', valor = '', dataVenc = '', dataPag = '', valorPag = '', devendo = '', status = ''):

        self.id = id
        self.desc = desc
        self.valor = valor
        self.dataVenc = dataVenc
        self.dataPag = dataPag
        self.valorPag = valorPag
        self.devendo = devendo
        self.status = status

        print(self.desc)
        cur.execute(f"UPDATE financa SET desc='{self.desc}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE financa SET valor='{self.valor}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE financa SET dataVenc='{self.dataVenc}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE financa SET dataPag='{self.dataPag}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE financa SET valorPag='{self.valorPag}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE financa SET devendo='{self.devendo}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE financa SET status='{self.status}' WHERE id = '{self.id}'")

        conn.commit()



# Função para Selecionar dados para que possa atualizar
def selecionar (linha):
    from TelaAtualizar import select
    cur.execute("SELECT id FROM financa")
    c = cur.fetchall()
    id = c[linha][0]
    cur.execute(f"SELECT * FROM financa where id = {id}")
    dado = cur.fetchall()

    conn.commit()

    return select(dado)





verify = cur.execute("SELECT name FROM sqlite_master WHERE name ='financa' ")

verify = cur.fetchone()

# Se a Tabela não for Criada no banco, executa a função create_sql()
if verify is None:
    ConectionForm().create_sql()


