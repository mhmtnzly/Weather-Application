import requests
from datetime import datetime
class Weather:
    def __init__(self):
        '&q=istanbul&days=3&aqi=no&alerts=no'
        self.api_key='2dbfd8657dcf46c7b09191433221601'
        self.api_url='https://api.weatherapi.com/v1/forecast.json?key='
    def get_weather(self,city_name,days):
        self.response=requests.get(self.api_url+self.api_key+'&q='+city_name+'&days='+days+'&aqi=no&alerts=no').json()
        return self.response
    def get_update_date(self):
        date=self.response['current']['last_updated']
        return date
    def current_weather(self):
        current=self.response['current']['condition']
        text=current['text']
        icon=current['icon'].split('/')[-2:]
        return text,icon

a=Weather()
c=a.get_weather('Amsterdam','1')
print(a.current_weather())