from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from ConexaoBD import ConectionForm
from ConexaoBD import  selecionar
from  TelaAlertaDelete import recebe_dados_excluir
from PyQt5.QtWidgets import *
from TelaSalvarRelatorio import TelaSalvarR

class TelaConsultar(object):
    def setupConsultar(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 454)
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
        self.pushButton.setGeometry(QtCore.QRect(30, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 400, 75, 23))
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
        self.pushButton_3.setGeometry(QtCore.QRect(120, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 400, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 0, 127);\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(170, 0, 255);\n"
                                        "")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("C:\\Users\\Deyvid\\Desktop\\ArquivosUI\\../Repo-GitHub/ControllFinance/seta-esquerda01.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 60, 71, 21))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 10, 91, 71))
        self.label_7.setText("")
        self.label_7.setPixmap(
            QtGui.QPixmap("C:\\Users\\Deyvid\\Desktop\\ArquivosUI\\../Repo-GitHub/ControllFinance/finance.png"))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton_3.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_4.setText(_translate("MainWindow", "Gerar Planilha Excel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "04/2021"))
        self.comboBox.setItemText(1, _translate("MainWindow", "05/2021"))
        self.comboBox.setItemText(2, _translate("MainWindow", "06/2021"))
        self.comboBox.setItemText(3, _translate("MainWindow", "07/2021"))
        self.comboBox.setItemText(4, _translate("MainWindow", "08/2021"))
        self.comboBox.setItemText(5, _translate("MainWindow", "09/2021"))
        self.comboBox.setItemText(6, _translate("MainWindow", "10/2021"))
        self.comboBox.setItemText(7, _translate("MainWindow", "11/2021"))
        self.comboBox.setItemText(8, _translate("MainWindow", "12/2021"))
        self.label_2.setText(_translate("MainWindow", "Mostrar compras da data:"))

        # Botão Listar
        self.pushButton.clicked.connect(self.listar_dados)

        # Botão para abrir a tela de confirmação da exclusão
        self.pushButton_2.clicked.connect(self.visualizar_alerta_delete)

        # Botão Atualizar
        self.pushButton_3.clicked.connect(self.tela_atualizar_dados)

        # Botão Gerar Relatório Excel
        self.pushButton_4.clicked.connect(self.open_save)



    def listar_dados(self):
        table = self.tableWidget
        data = self.comboBox.currentText()
        return ConectionForm().listar(data,table)

    def visualizar_alerta_delete(self):
        linha = self.tableWidget.currentRow()
        data = self.comboBox.currentText()
        return recebe_dados_excluir(data,linha)

    def tela_atualizar_dados(self):
        linha = self.tableWidget.currentRow()
        data = self.comboBox.currentText()
        return selecionar(data,linha)

    #Escolhe onde será salvo o local do arquivo Excel
    def open_save(self):
        data = self.comboBox.currentText()
        d = data.replace("/", '-') #Muda a data de: / para: -
        from GerarRelatorio import GerarPlanilha

        widget = QWidget()
        option = QFileDialog.Options()
        file = QFileDialog.getSaveFileName(widget, "Salve o arquivo em um local", f"ControleFinanceiro-{d}.xlsx", "All Files(*)", options=option)
        if file:
            self.tela_relatorio = TelaSalvaRelatorio()
            self.tela_relatorio.show() # mostra o form TelaSalvarRelatorio.py
            return GerarPlanilha().gerar_pla(data, file[0])

#Classe para chamar o script TelaSalvaRelatorio.py
class TelaSalvaRelatorio(QMainWindow):
   def __init__(self, *args, **argvs):
       super(TelaSalvaRelatorio, self).__init__(*args, **argvs)
       self.ui = TelaSalvarR()
       self.ui.setupRelatorio(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaConsultar()
    ui.setupConsultar(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
