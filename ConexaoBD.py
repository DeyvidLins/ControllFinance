import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import re

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


class Finance():
    # Função para Criar as tabelas no banco
    def create_sql(self):
        cur.execute('''CREATE TABLE finance(id INTEGER PRIMARY KEY AUTOINCREMENT, desc VARCHAR(100) NOT NULL, 
                   valor FLOAT NOT NULL,  dataVenc date NOT NULL,  dataPag date NOT NULL, valorPag FLOAT NOT NULL,
                   devendo  FLOAT NOT NULL, status varchar(2), cpf varchar(15) NOT NULL, FOREIGN KEY (cpf) REFERENCES users(cpf));''')
        conn.commit()

    # Função para Inserir dados
    def inserir (self,desc = '', valor = '', dataVenc = '', dataPag = '', valorPag = '', status = ''):

        if re.search('\\,\\b', valor, re.IGNORECASE): #Serve para fazer um procura de uma determinada letra na String(Neste caso à vírgula)
            v = valor.replace(',', '.')
        else:
            v = valor

        if re.search('\\,\\b', valorPag, re.IGNORECASE):
            vPag = valorPag.replace(',', '.')#Caso o usuário insira  vírgula substitui por ponto

        else:
            vPag = valorPag


        if valorPag == '':
            vPag = 0.00

        if dataPag == '':
            dataPag = 0


        sub = float(v) - float(vPag) # subtração do valor que está devendo
        dev = round(sub,2) # Arredonda o valor com apenas duas casas decimais
        self.desc = desc
        self.valor = float(v)
        self.dataVenc = dataVenc
        self.dataPag = dataPag
        self.valorPag = float(vPag)
        self.devendo = dev
        self.status = status

        #Insert SqlLite
        cur.execute(f'''INSERT INTO finance (desc,valor,dataVenc,dataPag,valorPag,devendo,status) 
                                                           VALUES ('{self.desc}','{self.valor}','{self.dataVenc}','{self.dataPag}',
                                                           '{self.valorPag}', '{self.devendo}', '{self.status}');''')
        conn.commit()

        # Este select é para pegar o Id do Banco Local(SqlLite) e enviar para o FireBase
        id = cur.execute(f'''SELECT id FROM finance WHERE desc = "{self.desc}" AND valor = {self.valor} AND dataVenc = "{self.dataVenc}"  AND
                         dataPAg= "{self.dataPag}" AND valorPag ={self.valorPag} AND devendo = {self.devendo} AND status="{self.status}" ''').fetchall()
        conn.commit()

        #Insert Firebase
        bd.child("Finance").push({"id":f"{id[0][0]}","descricao": f"{self.desc}", "valor": f"{self.valor}",
                                                     "dataVencimento": f"{self.dataVenc}",
                                                     "dataPagamento": f"{self.dataPag}",
                                                     "valorPago": f"{self.valorPag}",
                                                     "devendo": f"{self.devendo}",
                                                     "status": f"{self.status}"})

    # Função para Listar dados
    def listar(self, data, table):

        # Retorna uma lista do sql
        conn = sqlite3.connect('Financeiro.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM finance WHERE dataVenc LIKE '%{data}'")
        c = cur.fetchall()
        table.setRowCount(len(c))
        table.setColumnCount(8)


        for i in range(0, len(c)):
            for j in range(0, 8):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))

        conn.commit()

    # Função para Excluir dados
    def excluir(self, data, linha):
        cur.execute(f"SELECT id FROM finance WHERE dataVenc like '%{data}' ")
        c = cur.fetchall()
        id = c[linha][0]
        cur.execute(f"delete from finance where id = {id}")
        conn.commit()

        #FireBase Delete
        finance = bd.child("Finance").order_by_child("id").equal_to(f"{id}").get()
        for f in finance.each():
            fi = f.key()
            bd.child("Finance").child(f"{fi}").remove()

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


        cur.execute(f"UPDATE finance SET desc='{self.desc}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE finance SET valor='{self.valor}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE finance SET dataVenc='{self.dataVenc}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE finance SET dataPag='{self.dataPag}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE finance SET valorPag='{self.valorPag}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE finance SET devendo='{self.devendo}' WHERE id = '{self.id}'")
        cur.execute(f"UPDATE finance SET status='{self.status}' WHERE id = '{self.id}'")
        conn.commit()

        #FireBase update
        finance = bd.child("Finance").order_by_child("id").equal_to(f"{self.id}").get()
        for f in finance.each():
            fi = f.key()

            bd.child("Finance").child(f"{fi}").update({"descricao": f"{self.desc}"})
            bd.child("Finance").child(f"{fi}").update({"valor": f"{self.valor}"})
            bd.child("Finance").child(f"{fi}").update({"dataVencimento": f"{self.dataVenc}"})
            bd.child("Finance").child(f"{fi}").update({"dataPagamento": f"{self.dataPag}"})
            bd.child("Finance").child(f"{fi}").update({"valorPago": f"{self.valorPag}"})
            bd.child("Finance").child(f"{fi}").update({"devendo": f"{self.devendo}"})
            bd.child("Finance").child(f"{fi}").update({"status": f"{self.status}"})

# Função para Selecionar dados para que possa atualizar
def selecionar (data, linha):
    from TelaAtualizar import select
    cur.execute(f"SELECT id FROM finance WHERE dataVenc like '%{data}' ")
    c = cur.fetchall()
    id = c[linha][0]
    cur.execute(f"SELECT * FROM finance where id = {id}")
    dado = cur.fetchall()
    conn.commit()

    return select(dado)

class User():
    def create_sql(self):
        cur.execute('''CREATE TABLE users (cpf varchar(15) PRIMARY KEY NOT NULL, nome VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL,
                        sexo char(1) NOT NULL, dataNasc DATE NOT NULL, senha VARCHAR(10) NOT NULL);''')

        conn.commit()

    def inserir(self, cpf='', nome='', email='', sexo='', dataNasc='', senha=''):

        self.cpf = cpf
        self.nome =  nome
        self.email = email
        self.sexo = sexo
        self.dataNasc = dataNasc
        self.senha = senha


        # Insert SqlLite
        cur.execute(f'''INSERT INTO users (cpf,nome,email,sexo,dataNasc,senha) 
                        VALUES ('{self.cpf}','{self.nome}','{self.email}','{self.sexo}',
                        '{self.dataNasc}', '{self.senha}');''')
        conn.commit()

        # Este select é para pegar o Id do Banco Local(SqlLite) e enviar para o FireBase
        cpf = cur.execute(f'''SELECT cpf FROM users WHERE cpf= "{self.cpf}" AND nome= "{self.nome}" AND email= "{self.email}"  AND
                                 sexo= "{self.sexo}" AND dataNasc="{self.dataNasc}" AND senha= "{self.senha}" ''').fetchall()
        conn.commit()

        # Insert Firebase
        bd.child("Users").push({"cpf": f"{cpf[0][0]}", "nome": f"{self.nome}", "email": f"{self.email}","sexo": f"{self.sexo}",
                                  "dataNasc": f"{self.dataNasc}", "senha": f"{self.senha}"})



#----------------------------------Verifica se Existi à tabela FINANCE no Banco de Dados-----------------------------------------------------------------------

verify = cur.execute("SELECT name FROM sqlite_master WHERE name ='finance' ")
verify = cur.fetchone()
# Se a Tabela não for Criada no banco, executa a função create_sql()
if verify is None:
    Finance().create_sql()

#----------------------------------Verifica se Existi à tabela USER no Banco de Dados-----------------------------------------------------------------------
verify = cur.execute("SELECT name FROM sqlite_master WHERE name ='users' ")
verify = cur.fetchone()
# Se a Tabela não for Criada no banco, executa a função create_sql()
if verify is None:
    User().create_sql()