import pymysql

host = "sql12.freesqldatabase.com"
user = "sql12796732"
password = "WMEibZTbtC"
db = "sql12796732"

def db_connect():
  try:
    conn = pymysql.connect(host=host,user=user,password=password,db=db,port=3306)
    return conn
     
  except pymysql.MySQLError as e:
    print("Error connecting to databse ", e)
    return None
