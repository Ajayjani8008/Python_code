import mysql.connector 
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "student")
cur=myconn.cursor()  


try:
    cur.execute("update stu set name='amit' where name='ajay'")
    myconn.commit()
except:
    myconn.rollback()


myconn.close()  
  