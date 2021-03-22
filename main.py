from openpyxl import Workbook # pip install openpyxl
from openpyxl.styles import Font, Color, colors
#import pandas as pd



listDesc=["Descrição"]
listValor=["Valor"]
listData=["Data de Vencimento"]
listPag=["Data que foi pago"]
listValorPag=["Valor pago"]
listDev=["Devendo"]
listStatus=["Status"]


wb = Workbook()
ws1 = wb.active # work sheet
ws1.title = "Pyxl"

# Realiza a leitura  do arquvio excel através da biblioteca Pandas
#x = pd.read_excel(r"C:\Users\Deyvid\Desktop\Repo-GitHub\pythonExcel\ControleFinanceiro.xlsx")
#print(x)

ws1.cell(column=1, row=1, value=listDesc[0])
ws1.cell(column=2, row=1, value=listValor[0])
ws1.cell(column=3, row=1, value=listData[0])
ws1.cell(column=4, row=1, value=listPag[0])
ws1.cell(column=5, row=1, value=listValorPag[0])
ws1.cell(column=6, row=1, value=listDev[0])
ws1.cell(column=7, row=1, value=listStatus[0])


cont = 1
info = input('Deseja continuar? Digite C para continuar e S para sair:')
while True:

    if info.lower() =="c" or info.upper() == "C":

        desc = input('Digite à descrição do produto:')
        listDesc.append(desc)
        for i in range (1,len(listDesc)):
            ws1.cell(column=1, row=i+ 1, value=listDesc[i])


        valor = float(input(f'Digite o valor do produto {desc}:'))
        listValor.append(valor)
        for i in range (1,len(listValor)):
            ws1.cell(column=2, row=i + 1, value=listValor[i])

        dataVenc = input(f'Digite a data de Vencimento do produto {desc}:')
        listData.append(dataVenc)
        for i in range (1,len(listData)):
            ws1.cell(column=3, row=i+ 1, value=listData[i])

        pag = input(f'Informe a data que foi realizado o pagamento do produto {desc}:')
        listPag.append(pag)
        for i in range (1,len(listPag)):
            ws1.cell(column=4, row=i + 1, value=listPag[i])

        valorPag = float(input(f'Informe o valor que foi pago do produto {desc}:'))
        listValorPag.append(valorPag)
        for i in range (1,len(listValor)):
            ws1.cell(column=5, row=i+ 1, value=listValorPag[i])

        devendo = float(listValor[cont]- listValorPag[cont])
        listDev.append(devendo)
        for i in range (1,len(listDev)):
            ws1.cell(column=6, row=i+ 1, value=listDev[i])

        status = input(f'Infome PG para PAGO ou NP para NÃO PAGO:')
        listStatus.append(status.upper())
        for i in range (1,len(listStatus)):
            ws1.cell(column=7, row=i + 1, value=listStatus[i])

        cont +=1

    elif info.lower()=="s" or info.upper() == "S":
        print ('Saindo....')
        break
    else:
        print('Saindo....')
        break
    info = input('Deseja continuar? Digite C para continuar e S para sair:')




ws1["H13"]='TOTAL'
ws1["I13"]='=SUM(F2:B50)'


ft_a = Font(name='Times New Roman',color=colors.BLACK, bold=True, size=12)

a1 = ws1['A1']
b1 = ws1['B1']
c1 = ws1['C1']
d1 = ws1['D1']
e1 = ws1['E1']
f1 = ws1['F1']
g1 = ws1['G1']
h13 = ws1['H13']
a1.font = ft_a
b1.font = ft_a
c1.font = ft_a
d1.font = ft_a
e1.font = ft_a
f1.font = ft_a
g1.font = ft_a
h13.font = ft_a

wb.save('ControleFinanceiro.xlsx')

