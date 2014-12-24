import mysql.connector

class WebSite:
    def __init__(self):
        self.db = mysql.connector.connect(
            user='root', passwd='271828', db='mysite5_db', 
            host='127.0.0.1', charset="utf8",  use_unicode=True, raise_on_warnings=False
        )
        self.cursor = self.db.cursor()
        self.items = []
        self.get_items_from_db()

        for i in self.items:
            print i

    def get_items_from_db(self):
        self.cursor.execute("SELECT * FROM WebPage_website")
        self.items = self.cursor.fetchall()

    def get_allowed_domains(self):
        return [i[2] for i in self.items]
           
    def get_start_urls(self):
        return [i[3] for i in self.items]
