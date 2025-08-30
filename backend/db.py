import pymysql

host = "sql213.infinityfree.com "
user = "if0_39826194"
password = "X9v5HUsZtVZEF"
db = "if0_39826194_snektestingdb"

def db_connect():
  try:
    conn = pymysql.connect(host=host,user=user,password=password,db=db,port=3306)
    return conn
     
  except pymysql.MySQLError as e:
    print("Error connecting to databse ", e)
    return None
