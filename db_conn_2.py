from PyQt5 import QtWidgets,uic
import db_conn
import psycopg2

class Weather_window(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(Weather_window, self).__init__() 
        uic.loadUi('ui/weatherapp.ui', self)
        self.search.clicked.connect(self.Search)
        self.usa.clicked.connect(self.Usa)
        self.nl.clicked.connect(self.Nl)
        self.tr.clicked.connect(self.Tr)
        self.show()

    def Search(self):
        c_search = db_conn.Weather_db()
        info = c_search.name_search()
        self.city.setText(f'{str(info[0][0])}')
        self.population.setText(f'{str(info[0][1])}')
        self.province.setText(f'{str(info[0][2])}')

    def Usa(self):
        c_search = db_conn.Weather_db()
        info = c_search.usa_click()
        self.liste.setText(f'{str(info)}')

    def Nl(self):
        c_search = db_conn.Weather_db()
        info = c_search.nl_click()
        self.liste.setText(f'{str(info)}')

    def Tr(self):
        c_search = db_conn.Weather_db()
        info = c_search.tr_click()
        self.liste.setText(f'{str(info)}')



        city = self.city_name.text()
        print(city)
        self.cur.execute(""" 
            SELECT city, region, population FROM places where city = 'Ankara';
            """)
        info = self.cur.fetchall() # you can also use fetchone() and fetchmany() according to your need
        print(info)