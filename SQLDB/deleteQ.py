import mysql.connector 
  

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "student")    
  

cur = myconn.cursor()  
  
try:  
    cur.execute("delete from  stu where name='amit'")  
    myconn.commit()
   
 
except:  
    myconn.rollback()  
myconn.close()  