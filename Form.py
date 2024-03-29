from PyQt5 import QtCore, QtGui, QtWidgets
from ConexaoBD import ConectionForm


class TelaInserir(object):
    def setupInserir(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 494)
        MainWindow.setStyleSheet("background-color: rgb(174, 142, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 330, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 410, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 120, 321, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 160, 141, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 280, 121, 21))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(210, 200, 110, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setDate(QtCore.QDate(2021, 4, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 330, 69, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 240, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 10, 91, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(
            QtGui.QPixmap("C:\\Users\\Deyvid\\Desktop\\ArquivosUI\\../Repo-GitHub/ControllFinance/finance.png"))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        self.menuConsultar_Compras_D_vidas = QtWidgets.QMenu(self.menubar)
        self.menuConsultar_Compras_D_vidas.setObjectName("menuConsultar_Compras_D_vidas")
        MainWindow.setMenuBar(self.menubar)
        self.actionConsultar = QtWidgets.QAction(MainWindow)
        self.actionConsultar.setObjectName("actionConsultar")
        self.actionAtualizar_comprar_D_vidas = QtWidgets.QAction(MainWindow)
        self.actionAtualizar_comprar_D_vidas.setObjectName("actionAtualizar_comprar_D_vidas")
        self.menuConsultar_Compras_D_vidas.addAction(self.actionConsultar)
        self.menubar.addAction(self.menuConsultar_Compras_D_vidas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Controle Financeiro"))
        self.label_2.setText(_translate("MainWindow", "Descrição da Compra/Produto:"))
        self.label_3.setText(_translate("MainWindow", "Valor da compra/Produto:"))
        self.label_4.setText(_translate("MainWindow", "Data de Vencimento:"))
        self.label_5.setText(_translate("MainWindow", "Data de Pagamento:"))
        self.label_6.setText(_translate("MainWindow", "Valor pago:"))
        self.label_8.setText(_translate("MainWindow", "Pagou a fatura/Produto?"))
        self.pushButton.setText(_translate("MainWindow", "Salvar"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Sim"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Não"))
        self.menuConsultar_Compras_D_vidas.setTitle(_translate("MainWindow", " Compras/Dívidas"))
        self.actionConsultar.setText(_translate("MainWindow", "Consultar"))
        self.actionAtualizar_comprar_D_vidas.setText(_translate("MainWindow", "Atualizar comprar/Dívidas"))

        # Botão Salvar
        self.pushButton.clicked.connect(self.inserir_dados)

    # Lançamento dos dados para o banco
    def inserir_dados(self):

        desc = self.lineEdit.text()
        valor = self.lineEdit_2.text()
        dataVenc = self.dateEdit.text()
        dataPag = self.lineEdit_3.text()
        valorPag = self.lineEdit_5.text()
        status = self.comboBox.currentText()
        c = ConectionForm().inserir(desc,valor,dataVenc,dataPag,valorPag,status)

        return  c


    def test_inserir(self, listaDados):

        if listaDados[4] == '':
            listaDados[4] = 0.00

        if listaDados[3] == '':
            listaDados[3] = 0



        desc = listaDados[0]
        valor = float(listaDados[1])
        dataVenc = listaDados[2]
        dataPag = listaDados[3]
        valorPag = float(listaDados[4])
        sub = valor - valorPag  # subtração do valor que está devendo
        dev = round(sub, 2)
        status = listaDados[5]

        co = (desc, valor, dataVenc, dataPag, valorPag, dev, status)
        print(co)

        return co



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaInserir()
    ui.setupInserir(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())