from PyQt5 import QtCore, QtGui, QtWidgets
from ConexaoBD import ConectionForm


class TelaAlertaDel(object):
    def setupAlertaDelete(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 250)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 160, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Você realmente deseja excluir? "))
        self.pushButton.setText(_translate("MainWindow", "Sim"))
        self.pushButton_2.setText(_translate("MainWindow", "Não"))
        self.label_2.setText(_translate("MainWindow", "Obs.: Ao Confirmar você não poderá voltar atrás."))

        # Botão Confirmar À exclusão
        self.pushButton.clicked.connect(self.excluir_dados)


    def excluir_dados(self):

        return ConectionForm().excluir(n)


n = 5 # Pode ser um valor qualquer
def recebe_dados_excluir(linha):
    global n
    n = linha



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaAlertaDel()
    ui.setupAlertaDelete(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
