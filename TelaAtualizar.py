from PyQt5 import QtCore, QtGui, QtWidgets
from ConexaoBD import ConectionForm


class TelaUpdate(object):
    def setupUpdate(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 193)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 30, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 30, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 30, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 30, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(710, 30, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 30, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 41, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 60, 91, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 60, 61, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 60, 151, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 60, 161, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(520, 60, 91, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 60, 91, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(700, 60, 61, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Salvar"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Descrição"))
        self.label_3.setText(_translate("MainWindow", "Valor"))
        self.label_4.setText(_translate("MainWindow", "Data de Vencimento"))
        self.label_5.setText(_translate("MainWindow", "Data de Pagamento"))
        self.label_6.setText(_translate("MainWindow", "Valor pago"))
        self.label_7.setText(_translate("MainWindow", "Status"))
        self.label_8.setText(_translate("MainWindow", "Devendo"))

        self.lineEdit.setText(f'{l[0]}')  # Descrição
        self.lineEdit_2.setText(f'{l[1]}') # Descrição
        self.lineEdit_3.setText(f'{l[2]}') # valor
        self.lineEdit_4.setText(f'{l[3]}') # Data Vencimento
        self.lineEdit_5.setText(f'{l[4]}') # Data de Pagamento
        self.lineEdit_6.setText(f'{l[5]}') # Valor pago
        self.lineEdit_7.setText(f'{l[6]}') # Devendo
        self.lineEdit_8.setText(f'{l[7]}') # Status

        self.pushButton.clicked.connect(self.atualizar_dados)


    def atualizar_dados(self):
        c = ConectionForm().atualizar(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),
                                      self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(),
                                      self.lineEdit_7.text(), self.lineEdit_8.text())

        return c


lista = [] # lista vazia para receber uma lista de tuplas
def select(dado):
    global lista
    #Conversão de uma lista de tuplas para lista simples
    id = dado[0][0]
    desc = dado[0][1]
    valor = dado[0][2]
    dataVenc = dado[0][3]
    dataPag = dado[0][4]
    valorPag = dado[0][5]
    devendo = dado[0][6]
    status = dado[0][7]
    lista = [id, desc, valor, dataVenc, dataPag, valorPag, devendo, status]

    return select_01()

l = ['']
def select_01():
    global l # Variável global. Em vez de ser uma lista vazia, será uma lista com os valores abaixo
    id  = lista[0]
    desc = lista[1]
    valor = lista[2]
    dataVenc = lista[3]
    dataPag = lista[4]
    valorPag = lista[5]
    devendo = lista[6]
    status =  lista[7]
    l = [id,desc,valor, dataVenc, dataPag, valorPag, devendo, status]

    return l

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaUpdate()
    ui.setupUpdate(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())