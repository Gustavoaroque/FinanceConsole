import uuid 
import psycopg2

import os


cursor = None
conn= None

class DatabaseManager:
    def __init__(self,db_name,db_user,db_password,db_host,db_port):
        print(f"{db_name},{db_user},{db_password},{db_port},{db_host}")
        self.connection  = psycopg2.connect(
            dbname = db_name,
            user =db_user,
            password = db_password,
            host = db_host,
            port = db_port
            )
        self.cursor = self.connection.cursor()
        
    def Create(self, table, cols , data):
        """"
        Insert data into tables
        param table: table Name
        param data: Dictionary {columnName: value}
        
        """

        #Learn about dict methods
        columns  = ", ".join(cols)
        placeholders = ", ".join(['%s'] * len(data))

        sqlquery = f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"
        # print(sqlquery,data)
        self.cursor.execute(sqlquery,data)
        self.connection.commit()
        
    def Read(self,table):
        sqlquery = f"SELECT * FROM {table};"
        self.cursor.execute(sqlquery)
        return self.cursor.fetchall()



