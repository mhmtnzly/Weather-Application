import requests
import geocoder


class Weather:

    def __init__(self):
        self.api_key = '2dbfd8657dcf46c7b09191433221601'
        self.api_url = 'https://api.weatherapi.com/v1/forecast.json?key='
    
    def my_location(self):
        g = geocoder.ip('me')
        return g.city
        
    def get_weather(self,city_name,days):
        self.response = requests.get(self.api_url+self.api_key+'&q='+city_name+'&days='+days+'&aqi=no&alerts=no').json()
        return self.response

    def current_weather(self):
        current = self.response['current']
        condition = current ['condition']
        self.last_update = current['last_updated']
        text = condition['text']
        icon = condition['icon'].split('/')[-2:]
        degree = current['temp_c']
        return self.last_update,text,degree,icon

    def days_forecast(self):
        forecastday = self.response['forecast']['forecastday']
        days = []
        for day in forecastday:
            date = day['date']
            day_ = day['day']
            maxtemp_c = day_['maxtemp_c']
            mintemp_c = day_['mintemp_c']
            condtion = day_['condition']
            text = condtion['text']
            icon = condtion['icon'].split('/')[-2:]
            days.append([date,text,maxtemp_c,mintemp_c,icon])
        return days
    
    
    def hours_forecast(self):
        forecastday = self.response['forecast']['forecastday']
        hour_forecast = []
        for day in forecastday:
            for hour in day['hour']:
                if hour['time']>self.last_update:
                    time = hour['time'].split()[1]
                    temp_c = hour['temp_c']
                    condtion = hour['condition']
                    text = condtion['text']
                    icon = condtion['icon'].split('/')[-2:]
                    hour_forecast.append([time,temp_c,text,icon])
        return hour_forecast[:4]
