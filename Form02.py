from PyQt5 import QtCore, QtGui, QtWidgets
from ConexaoBD import ConectionForm
from ConexaoBD import  selecionar
from  TelaAlertaDelete import recebe_dados_excluir



class TelaConsultar(object):
    def setupConsultar(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 499)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 821, 291))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 420, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 420, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 420, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 21))
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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID do Registro"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descrição"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data de Vencimento"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data de Pagamento"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Valor Pago"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Devendo"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Lista de Compras/Produtos"))
        self.pushButton.setText(_translate("MainWindow", "Listar"))
        self.pushButton_2.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_3.setText(_translate("MainWindow", "Atualizar"))
        self.pushButton_4.setText(_translate("MainWindow", "Gerar Planilha Excel"))

        # Botão Listar
        self.pushButton.clicked.connect(self.listar_dados)

        # Botão para abrir a tela de confirmação da exclusão
        self.pushButton_2.clicked.connect(self.visualizar_alerta_delete)

        # Botão Atualizar
        self.pushButton_3.clicked.connect(self.tela_atualizar_dados)

        # Botão Gerar Relatório Excel
        self.pushButton_4.clicked.connect(self.gerar_planilha)

    def listar_dados(self):
        table = self.tableWidget
        return ConectionForm().listar(table)

    def visualizar_alerta_delete(self):
        linha = self.tableWidget.currentRow()
        self.tableWidget.removeRow(linha)

        return recebe_dados_excluir(linha)

    def tela_atualizar_dados(self):
        linha = self.tableWidget.currentRow()

        return selecionar(linha)

    def gerar_planilha(self):
        import GerarRelatorio
        GerarRelatorio
        print("Gerado com Sucesso")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaConsultar()
    ui.setupConsultar(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
