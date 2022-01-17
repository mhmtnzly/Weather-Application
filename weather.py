from PyQt5 import QtWidgets,uic,QtGui
import test_rc
from api import Weather




class Weather_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Weather_window, self).__init__() 
        uic.loadUi('ui/weatherapp.ui', self) 
        self.weather = Weather()
        location = self.weather.my_location()
        self.weather.get_weather(location,'3')
        self.days_forecast = self.weather.days_forecast()
        self.current_weather = self.weather.current_weather()
        self.hours_forecast = self.weather.hours_forecast()

        self.get()
        self.show()
    def get(self):
        self.today_condition.setText(self.days_forecast[0][1])
        self.degree.setText('({}-{})'.format(self.days_forecast[0][3],self.days_forecast[0][2]))
        self.w_icon.setPixmap(QtGui.QPixmap('{}/{}'.format(self.days_forecast[0][4][0],self.days_forecast[0][4][1])))
        
        self.tomorrow_condition.setText(self.days_forecast[1][1])
        self.degree_2.setText('({}-{})'.format(self.days_forecast[1][3],self.days_forecast[1][2]))
        self.w_icon_2.setPixmap(QtGui.QPixmap('{}/{}'.format(self.days_forecast[1][4][0],self.days_forecast[1][4][1])))
        
        self.day3.setText(self.days_forecast[2][0])
        self.after_tomorrow_condition.setText(self.days_forecast[2][1])
        self.degree_3.setText('({}-{})'.format(self.days_forecast[2][3],self.days_forecast[2][2]))
        self.w_icon_3.setPixmap(QtGui.QPixmap('{}/{}'.format(self.days_forecast[2][4][0],self.days_forecast[2][4][1])))
        

        self.hour1.setText(self.hours_forecast[0][0])
        self.hour2.setText(self.hours_forecast[1][0])
        self.hour3.setText(self.hours_forecast[2][0])
        self.hour4.setText(self.hours_forecast[3][0])

        self.h_icon1.setPixmap(QtGui.QPixmap('{}/{}'.format(self.hours_forecast[0][3][0],self.hours_forecast[0][3][1])))
        self.h_icon2.setPixmap(QtGui.QPixmap('{}/{}'.format(self.hours_forecast[1][3][0],self.hours_forecast[1][3][1])))
        self.h_icon3.setPixmap(QtGui.QPixmap('{}/{}'.format(self.hours_forecast[2][3][0],self.hours_forecast[2][3][1])))
        self.h_icon4.setPixmap(QtGui.QPixmap('{}/{}'.format(self.hours_forecast[3][3][0],self.hours_forecast[3][3][1])))

        self.h_degree1.setText(str(self.hours_forecast[0][1]))
        self.h_degree2.setText(str(self.hours_forecast[1][1]))
        self.h_degree3.setText(str(self.hours_forecast[2][1]))
        self.h_degree4.setText(str(self.hours_forecast[3][1]))

        self.h_condition1.setText(self.hours_forecast[0][2])
        self.h_condition2.setText(self.hours_forecast[1][2])
        self.h_condition3.setText(self.hours_forecast[2][2])
        self.h_condition4.setText(self.hours_forecast[3][2])
        
        print(self.current_weather)

        self.main_degree.setText(str(self.current_weather[2]))
        self.main_weather.setText(self.current_weather[1])
        self.main_icon.setPixmap(QtGui.QPixmap('{}/{}'.format(self.current_weather[3][0],self.current_weather[3][1])))
