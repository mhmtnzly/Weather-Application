import scrapy


class TurkeySpider(scrapy.Spider):
    name = 'turkey'
    #allowed_domains = ['https://tr.wikipedia.org/wiki/T%C3%BCrkiye'deki_illerin_n%C3%BCfuslar%C4%B1_(2020)']
    start_urls = ["https://tr.wikipedia.org/wiki/T%C3%BCrkiye'deki_illerin_n%C3%BCfuslar%C4%B1_(2020)/"]

    def parse(self, response):                                                                              
        city =  response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').css('td ::text').extract()       ### we choose city,region and population
        j = 0
        for j in range(0,324,4):
            city_name = city[j]
            region_name = city[j+2]
            population = city[j+1]
            yield{"city":city_name,"region":region_name,"population":population}