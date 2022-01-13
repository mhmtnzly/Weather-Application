from typing import Counter
import scrapy


class WeatherCondSpider(scrapy.Spider):
    name = 'weather_cond'
    # allowed_domains = ['https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten']
    #start_urls =  ['https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten']            ### NL
    #start_urls =  ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']                 ### USA
    #start_urls =  ["https://tr.wikipedia.org/wiki/T%C3%BCrkiye'deki_illerin_n%C3%BCfuslar%C4%B1_(2020)"]       ### TUR
    

    """def parse(self, response):                                                                               ### NL
        counter = 2
        while counter < 188:                                                                                      
            city =  response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[{counter}]').css('td ::text').extract()
            j = 0
            for j in range(0,640,640):
                print([city[j],city[j+1]])
            counter += 1
        print("#######NL#######")"""


    """def parse(self, response):                                                                                ### USA KULLANILACAK
        city =  response.xpath('//*[@id="mw-content-text"]/div[1]/table[5]/tbody/tr').css('td ::text').extract()
        i = 0
        s1=''
        while i < len(city):
            s1=s1+' '+city[i]
            i+=1
        s1 = s1.split('\n')
        j = 0
        for j in range(0,3260,10):
            print([s1[j],s1[j+1],s1[j+2]])
        print("#######USA#######")"""



    """def parse(self, response):                                                                               ### TUR KULLANILACAK
        city =  response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').css('td ::text').extract()
        j = 0
        for j in range(0,324,4):
            print([city[j],city[j+2],city[j+1]])
        print("#######TUR#######")"""