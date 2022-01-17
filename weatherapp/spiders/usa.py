import scrapy


class UsaSpider(scrapy.Spider):
    name = 'usa'
    #allowed_domains = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population/']

    def parse(self, response):                                                                               
        city = response.xpath('//*[@id="mw-content-text"]/div[1]/table[5]/tbody').css('tr')                 ### we choose city,region and population
        for i in city[1:]:
            data = i.css('td ::text').extract()
            city_name = data[0]
            if "[" in data[1]:
                region_name = data[3]
                population = data[5]
                population = population.replace(',','')
            else:
                region_name = data[2]
                population = data[4]
                population = population.replace(',','')
                
                if len(population) == 7:
                    population = population[:6]
                elif len(population) == 8:
                    population =population[:7]
                yield{"city":city_name,"region":region_name,"population":population}