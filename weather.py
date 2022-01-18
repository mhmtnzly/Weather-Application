from PyQt5 import QtWidgets,uic,QtGui
import test_rc
from api import Weather
from db_conn import Weather_db




class Weather_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Weather_window, self).__init__() 
        uic.loadUi('ui/weatherapp.ui', self) 
        self.weather = Weather()
        self.db = Weather_db()
        self.location = self.weather.my_location()
        
        self.table.cellClicked.connect(self.x)
        

        self.search.clicked.connect(self.search_db)

        self.usa.clicked.connect(self.load_usa)
        self.nl.clicked.connect(self.load_nl)
        self.tr.clicked.connect(self.load_tr)

        self.get()
        
        self.show()

    def x(self,row,col):
        print(row,col)
        print(self.table.cellWidget(row,col))
    def get(self):
        self.weather.get_weather(self.location,'3')
        self.days_forecast = self.weather.days_forecast()
        self.current_weather = self.weather.current_weather()
        self.hours_forecast = self.weather.hours_forecast()

        searching = self.db.name_search(self.location)
        self.city.setText(searching[0][0])
        self.province.setText(searching[0][1])
        self.population.setText(str(searching[0][2]))


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
        

        self.main_degree.setText(str(self.current_weather[2]))
        self.main_weather.setText(self.current_weather[1])
        self.main_icon.setPixmap(QtGui.QPixmap('{}/{}'.format(self.current_weather[3][0],self.current_weather[3][1])))
    
    def search_db(self):
        city_name_db = self.city_name.text()
        searching = self.db.name_search(city_name_db)
        
        
        if len(searching) > 0:
            city_name = searching[0][0]
            population = searching[0][2]
            province = searching[0][1]
            self.city.setText(city_name)
            self.province.setText(province)
            self.population.setText(str(population))
            self.location = city_name
            self.get()


    def load_usa(self):
        info = Weather_db()
        usa = info.country_click('USA')
        self.table.setRowCount(0)
        for row_number,row_data in enumerate(usa):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
    
    def load_nl(self):
        info = Weather_db()
        nl = info.country_click('NL')
        self.table.setRowCount(0)
        for row_number,row_data in enumerate(nl):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))

    def load_tr(self):
        info = Weather_db()
        tr = info.country_click('TUR')
        self.table.setRowCount(0)
        for row_number,row_data in enumerate(tr):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
    
   


