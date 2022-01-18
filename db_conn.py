import psycopg2

class Weather_db:
    def __init__(self):
        self.connect()
    
    def connect(self):
        self.conn = psycopg2.connect(database = "Weather",user = "postgres",host = "localhost",password = "Halo107.")
        self.cur = self.conn.cursor()

    def name_search(self,city_name):
        
        self.cur.execute(f"""
            SELECT city, region, population FROM places  where city = '{x}';
            """)
        info = self.cur.fetchall()
        return info

    def country_click(self,country):

        self.cur.execute(""" 
            SELECT city, region, population FROM places where country = '{}' order by population desc;
            """.format(country))
        info = self.cur.fetchall()
        return info


