from weather import Weather_window
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = Weather_window()
app.exec_()