import scrapy


class WeatherCondSpider(scrapy.Spider):
    name = 'weather_cond'
    ek_city = 'Lijst_van_Nederlandse_plaatsen_met_stadsrechten'
    # allowed_domains = ['https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten']
    #start_urls =  ['https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten']            ### NL
    #start_urls =  ['https://nl.wikipedia.org/wiki/'+ek_city] 
    #start_urls =  ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']                 ### USA
    #start_urls =  ["https://tr.wikipedia.org/wiki/T%C3%BCrkiye'deki_illerin_n%C3%BCfuslar%C4%B1_(2020)"]       ### TUR
    

    """def parse(self, response):                                                                               ### NL
        counter = 2
        while counter < 188:                                                                                      
            city =  response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[{counter}]').css('td ::text').extract()
            j = 0
            for j in range(0,640,640):
                print("Insert into places(city,region,country) values("+"'"+city[j]+"'"+","+"'"+city[j+1]+"'"+","+"'"+"NL"+"'"+");")
            counter += 1
        print("#######NL#######")"""



    """def parse(self, response):                                                                                ### USA KULLANILACAK
        city = response.xpath('//*[@id="mw-content-text"]/div[1]/table[5]/tbody').css('tr')
        for i in city[1:]:
            veriler = i.css('td ::text').extract()
            şehir = veriler[0]
            if "[" in veriler[1]:
                bölge = veriler[3]
                pop = veriler[5]
                pop = pop.replace(',','')
            else:
                bölge = veriler[2]
                pop = veriler[4]
                pop = pop.replace(',','')
                
                if len(pop) == 7:
                    pop = pop[:6]
                elif len(pop) == 8:
                    pop =pop[:7]
                print("Insert into places(city,region,population,country) values("+"'"+şehir+"'"+","+"'"+bölge+"'"+","+pop.replace(',','')+","+"'"+"USA"+"'"+");")"""



    """def parse(self, response):                                                                               ### TUR KULLANILACAK
        city =  response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr').css('td ::text').extract()
        j = 0
        for j in range(0,324,4):
            print("Insert into places(city,region,population,country) values("+"'"+city[j]+"'"+","+"'"+city[j+2]+"'"+","+"'"+city[j+1]+","+"'"+"TUR"+"'"+");")
        print("#######TUR#######")"""
