from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from  PyQt5.Qt import Qt
from  PyQt5.QtCore import pyqtSlot
from  PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys
from Form import TelaInserir
from Form02 import TelaConsultar
from TelaAtualizar import  TelaUpdate

#Form.py
class TelaPincipal(QMainWindow):
    def __init__(self,*args,**argvs):
        super(TelaPincipal,self).__init__(*args,**argvs)
        self.ui = TelaInserir()
        self.ui.setupInserir(self)
        self.ui.actionConsultar.triggered.connect(self.tela02)

    # Função para chamar a segunda tela que é Form02.py
    def tela02(self):
        self.tela_sec = TelaSecundaria()
        self.tela_sec.show()
        TelaPincipal.hide(self)


#Form02.py
class TelaSecundaria(QMainWindow):
    def __init__(self,*args,**argvs):
        super(TelaSecundaria,self).__init__(*args, **argvs)
        self.ui = TelaConsultar()
        self.ui.setupConsultar(self)
        self.ui.pushButton_3.clicked.connect(self.tela_update)

    def tela_update(self):
        self.tela_up = TelaAtualizar()
        self.tela_up.show()



#TelaAtualizar.py
class TelaAtualizar(QMainWindow):
    def __init__(self,*args,**argvs):
        super(TelaAtualizar,self).__init__(*args, **argvs)
        self.ui = TelaUpdate()
        self.ui.setupUpdate(self)



app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = TelaPincipal()
    window.show()
sys.exit(app.exec_())
