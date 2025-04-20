import uuid 
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


cursor = None
conn= None

class DatabaseManager:
    def __init__(self,db_name,db_user,db_password,db_host,db_port):
        self.connection  = psycopg2.connect(
            db_name, db_user,db_password, db_host,db_port
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



