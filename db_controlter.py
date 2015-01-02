import mysql.connector

class DB_controlter:
    def __init__(self):
        self.db = mysql.connector.connect(
            user='root', passwd='271828', db='mysite5_db', 
            host='127.0.0.1', charset="utf8",  use_unicode=True, raise_on_warnings=False
        )
        self.cursor = self.db.cursor()
        
