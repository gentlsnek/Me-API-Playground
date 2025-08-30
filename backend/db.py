import pymysql

host = "localhost"
user = "root"
password = "password"
db = "me_api"

def db_connect():
  try:
    conn = pymysql.connect(host=host,user=user,password=password,db=db)
    return conn
     
  except pymysql.MySQLError as e:
    print("Error connecting to databse ", e)
    return None
