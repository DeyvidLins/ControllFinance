
import sqlite3
conn = sqlite3.connect('Financeiro.db')
cur = conn.cursor()


listDesc=[]
listValor=[]
listData=[]
listPag=[]
listValorPag=[]
listDev=[]
listStatus=[]



def create_sql(): # Funcao CRIAR
    cur.execute('''CREATE TABLE financa(id INTEGER PRIMARY KEY AUTOINCREMENT, desc VARCHAR(100) NOT NULL, 
               valor FLOAT NOT NULL,  dataVenc VARCHAR(15) NOT NULL,  dataPag varchar(15) NOT NULL, valorPag FLOAT NOT NULL,
               devendo  FLOAT NOT NULL, status varchar(2));''')
    conn.commit()



verify = cur.execute("SELECT name FROM sqlite_master where name ='financa' ")

verify = cur.fetchone()

if verify is None:
    create_sql()



cont = 0
info = input('Deseja continuar? Digite C para continuar e S para sair:')
while True:

    if info.lower() == "c" or info.upper() == "C":

        desc = input('Digite à descrição do produto:')
        listDesc.append(desc)


        valor = float(input(f'Digite o valor do produto {desc}:'))
        listValor.append(valor)


        dataVenc = input(f'Digite a data de Vencimento do produto {desc}:')
        listData.append(dataVenc)


        dataPag = input(f'Informe a data que foi realizado o pagamento do produto {desc}:')
        listPag.append(dataPag)


        valorPag = float(input(f'Informe o valor que foi pago do produto {desc}:'))
        listValorPag.append(valorPag)



        devendo = float(listValor[cont] - listValorPag[cont])
        listDev.append(devendo)


        status = input(f'Infome PG para PAGO ou NP para NÃO PAGO:')
        listStatus.append(status.upper())



        cur.execute(f'''INSERT INTO financa (desc,valor,dataVenc,dataPag,valorPag,devendo,status) 
                                           VALUES ('{listDesc[cont]}','{listValor[cont]}','{listData[cont]}','{listPag[cont]}','{listValorPag[cont]}', '{listDev[cont]}', '{listStatus[cont]}');''')

        conn.commit()
        cont += 1




    elif info.lower() == "s" or info.upper() == "S":
        print('Saindo....')
        break
    else:
        print('Saindo....')
        break
    info = input('Deseja continuar? Digite C para continuar e S para sair:')












