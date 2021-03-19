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
        list_of_names = ['Paul', 'frank']
        #prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute("delete from Friends where name in ({});".format(format_strings), list_of_names) #string interpolation %s
        connection.commit()
        
finally:
    # close the connection, regrdless if the above query was successful
    connection.close()
