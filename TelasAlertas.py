# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# Define class to to display an informational message
class FormInfoPlanilha(QMainWindow):
    def __init__(self):
        # Call the parent constructor
        super().__init__()
        # Create the messagebox object
        self.msg = QMessageBox()
        # Set the information icon
        self.msg.setIcon(QMessageBox.Information)
        # Set the main message
        self.msg.setText("Planilha salva com Sucesso!!!")
        # Set the title of the window
        self.msg.setWindowTitle("Informação de Salvamento")
        # Display the message box
        self.msg.show()

# Create app object and run the app
app = QApplication(sys.argv)
Win = FormInfoPlanilha()
app.exec()