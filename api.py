import requests
from datetime import datetime
from PIL import Image
class Weather:
    def __init__(self):
        self.api_key='875552e892c12b621740ef1a211464a7'
        self.api_url='http://api.openweathermap.org/data/2.5/weather?'
        self.url='https://openweathermap.org/img/wn/'
    def get_weather(self,city_name,country_code):
        self.response=requests.get(self.api_url+'q='+city_name+','+country_code+'&appid='+self.api_key).json()
        return self.response
    def date(self):
        date=self.response['dt']
        date=datetime.fromtimestamp(date / 1e0)
        d_date=date.strftime('%d-%b-%Y')
        d_time=date.strftime('%H:%M:%S')
        return d_date,d_time
    def weather(self):
        self.weather=self.response['weather'][0]['main']
        self.icon=self.response['weather'][0]['icon']
        self.degree=int(self.response['main']['feels_like']-273.15)
        return self.weather,self.degree
    def icon_show(self):
        image='{}@2x.png'.format(self.icon)
        Image.open(image).show()

a=Weather()
a.get_weather('Ankara','tr')
a.weather()
a.icon_show()