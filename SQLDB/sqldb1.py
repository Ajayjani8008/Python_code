import mysql.connector 
  

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "student")    
  

cur = myconn.cursor()  
  
try:  
    cur.execute("insert into stu values('ajay','abggc','12343','70167889')")  
    myconn.commit()
    cur.execute("insert into stu values('amit','xysdfz','145343','03784534169')")  
    myconn.commit()
 
    cur.execute("insert into stu values('manav','xdfyz','145433','07834534169')")  
    myconn.commit()

    cur.execute("insert into stu values('mahesh','xydfhz','1434353','03453784169')")  
    myconn.commit()
 
    cur.execute("insert into stu values('mahipal','dfjg','145433','034534169')")  
    myconn.commit()
 
except:  
    myconn.rollback()  
myconn.close()  