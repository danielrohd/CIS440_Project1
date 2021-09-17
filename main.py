# Main Script
"""
To use PyQt5:
pip install PyQt5
pip install pyqt5-tools

To open the designer:
qt5-tools designer
"""


from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    """Imports the UI file"""
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('AppUI.ui', self)
        self.show()


# Creates an instance of the UI and starts it
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
