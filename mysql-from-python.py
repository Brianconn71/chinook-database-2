import os
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
        sql = "Select * From Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection, regrdless if the above query was successful
    connection.close()
