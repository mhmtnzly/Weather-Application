import scrapy


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    #allowed_domains = ['https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten']
    start_urls =  ['https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten'] 


    def parse(self, response):                                                                               ### NL
        counter = 2
        while counter < 188:                                                                                      
            city =  response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[{counter}]').css('td ::text').extract()        ### we choose cityname,region
            pop = response.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td/a/@href').extract()                            ### we choose hrefs
            for j in range(0,640,640):
                city_name = city[j]
                region_name = city[j+1]
                for i in pop:
                    url=response.urljoin(i)
                    yield scrapy.Request(url,callback=self.detail)
            counter += 1
            yield{"city":city_name,"region":region_name}

    def detail(self,response):  
        print("***********************************")
        population = response.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr')                                              ### we choose population
        city_name = response.xpath('//*[@id="mw-content-text"]/div[1]/table[1]/caption/b').css('::text').extract()
        for j in population:
            p = j.css("td ::text").getall()
            if "Inwoners" in p:
                yield{"population":p[3],"city name":city_name}
            elif "Inwoners " in p:
                yield{"population":p[2],"city name":city_name}