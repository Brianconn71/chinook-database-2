import os
import datetime
import pymysql

#Get Username from workspace
username = os.getenv('GIT_USER')

#Connection to database

connection = pymysql.connect(host='localhost', 
                            user=username,
                            password = '',
                            db='Chinook')
try:
    #run a query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1994-02-06 23:04:56"),
                ("Jim", 45, "1974-02-06 20:04:56"),
                ("Paul", 50, "1974-02-06 20:04:56")]
        cursor.executemany("Insert into Friends Values(%s, %s, %s);", rows)
        connection.commit()
        
finally:
    # close the connection, regrdless if the above query was successful
    connection.close()
