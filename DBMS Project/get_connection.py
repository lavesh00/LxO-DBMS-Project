import cx_Oracle
from pymongo import MongoClient

# Oracle DB connection details
def get_oracle_connection():
    username = 'system'
    password = 'tiger'
    host = 'localhost'  
    port = '1521'       
    service_name = 'xe'
    
    dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
    connection = cx_Oracle.connect(username, password, dsn)
    return connection

# MongoDB connection details
def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['DBMS']
    return db['DBMS'] 
