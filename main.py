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
from TelaSalvar import  Tsalvar
from TelaAlertaDelete import TelaAlertaDel
from TelaApagar import TelaDelete


#Form.py
class TelaPincipal(QMainWindow):
    def __init__(self,*args,**argvs):
        super(TelaPincipal,self).__init__(*args,**argvs)
        self.ui = TelaInserir()
        self.ui.setupInserir(self)
        self.ui.actionConsultar.triggered.connect(self.tela02)
        self.ui.pushButton.clicked.connect(self.visualizar_salvar)

    # Função para chamar a segunda tela que é Form02.py
    def tela02(self):
        self.tela_sec = TelaSecundaria()
        self.tela_sec.show()
        TelaPincipal.hide(self)

    #Mostra na tela que foi salvo
    def visualizar_salvar(self):
        self.tela_sa = TelaSalve()
        self.tela_sa.show()



#TelaSalvar.py
class TelaSalve(QMainWindow):
    def __init__(self, *args, **argvs):
        super(TelaSalve, self).__init__(*args, **argvs)
        self.ui = Tsalvar()
        self.ui.setupSalvar(self)
        self.ui.pushButton.clicked.connect(self.encerrar_tela)

    def encerrar_tela(self):
        TelaSalve.hide(self)


#Form02.py
class TelaSecundaria(QMainWindow):
    def __init__(self,*args,**argvs):
        super(TelaSecundaria,self).__init__(*args, **argvs)
        self.ui = TelaConsultar()
        self.ui.setupConsultar(self)
        self.ui.pushButton_2.clicked.connect(self.visualizar_aletar_delete)
        self.ui.pushButton_3.clicked.connect(self.tela_update)

    def tela_update(self):
        self.tela_up = TelaAtualizar()
        self.tela_up.show()

    def visualizar_aletar_delete(self):
        self.tela_alert_delet = TelaAlertaD()
        self.tela_alert_delet.show()


#TelaAtualizar.py
class TelaAtualizar(QMainWindow):
    def __init__(self,*args,**argvs):
        super(TelaAtualizar,self).__init__(*args, **argvs)
        self.ui = TelaUpdate()
        self.ui.setupUpdate(self)
        self.ui.pushButton.clicked.connect(self.visualizar_salvar)

    def visualizar_salvar(self):
        self.tela_sa = TelaSalve()
        self.tela_sa.show()

#TelaAlertaDelete.py
class TelaAlertaD(QMainWindow):
    def __init__(self,*args,**argvs):
        super(TelaAlertaD,self).__init__(*args, **argvs)
        self.ui = TelaAlertaDel()
        self.ui.setupAlertaDelete(self)
        self.ui.pushButton.clicked.connect(self.confirma_sim)
        self.ui.pushButton_2.clicked.connect(self.confirma_nao)


    def confirma_sim(self):
        self.tela_conf_sim = TelaDelet()
        self.tela_conf_sim.show()

    def confirma_nao(self):
        TelaAlertaD.hide(self)

class TelaDelet(QMainWindow):
   def __init__(self, *args, **argvs):
       super(TelaDelet, self).__init__(*args, **argvs)
       self.ui = TelaDelete()
       self.ui.setupDel(self)




app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = TelaPincipal()
    window.show()
sys.exit(app.exec_())
