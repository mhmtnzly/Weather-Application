from PyQt5 import QtWidgets,uic
import test_rc

class Weather_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Weather_window, self).__init__() 
        uic.loadUi('ui/weatherapp.ui', self) 
        self.show() 