import sqlite3
import os

class SQL_handler:
    def commit_start(self):
        self.connect = sqlite3.connect('new.db')
        self.cur = self.connect.cursor()
        
    def commit_end(self):
        self.connect.commit()
        self.connect.close()  
    
    def table_create(self):
        self.commit_start()
        self.cur.execute("""        
        CREATE TABLE IF NOT EXISTS Web (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(100),
            password VARCHAR(100)
        )
                    """)
        self.commit_end()

    def add_new_values(self,email,paswword):
        self.commit_start()
        self.cur.execute(
            """INSERT INTO Web (email,password) VALUES (?,?)""",
            (email,paswword,)
        )
        self.commit_end()
        
    def check_duplicate(self,email):
        self.commit_start()
        try:
            self.cur.execute(
                """SELECT email FROM Web WHERE email=?""",
                (email,)
            )
            result = self.cur.fetchall()
            return True if result else False
        finally:
            self.commit_end()

    def check_login(self,email,password):
        self.commit_start()
        self.cur.execute("SELECT * FROM Web WHERE email=? AND password=?",(email,password))
        yes = self.cur.fetchone()
        return bool(yes)
    
    def make_sneakers(self):
        self.commit_start()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image VARCHAR(100),
            name VARCHAR(100),
            description VARCHAR(6000)
        )
                 """)
        self.commit_end()
        
    def add_sneakers(self):
        self.commit_start()
        self.cur.execute(
            """INSERT INTO Products (image,name,description) VALUES (?,?,?)""",
            ("1.jpg","jeremmyscott","jesus christ i cant live on this planet with such suffer and gross please excecuter me by lighnting bolt",)
        )
        self.commit_end()

    def make_readable(self,text):
        sex = text[2:-2:1]
        return sex
    

sex = SQL_handler()
sex.add_sneakers()