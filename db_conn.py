import psycopg2

class Weather_db:
    def __init__(self):
        self.connect()
    
    def connect(self):
        self.conn = psycopg2.connect(database = "weather",user = "postgres",host = "localhost",password = "Halo107.")
        self.cur = self.conn.cursor()

    def name_search(self,city_name):
        x= city_name.capitalize()
        self.cur.execute(f"""
            SELECT city, region, population FROM places  where city = '{x}';
            """)
        info = self.cur.fetchall()
        return info

    def usa_click(self):
        self.cur.execute(f""" 
            SELECT city, region, population FROM places where country = 'USA' order by population desc;
            """)
        info = self.cur.fetchall()
        return info
    
    def nl_click(self):
        self.cur.execute(f""" 
            SELECT city, region, population FROM places where country = 'NL' order by population desc;
            """)
        info = self.cur.fetchall()
        return info
    
    def tr_click(self):
        self.cur.execute(f""" 
            SELECT city, region, population FROM places where country = 'TUR' order by population desc;
            """)
        info = self.cur.fetchall()
        return info

weather = Weather_db
