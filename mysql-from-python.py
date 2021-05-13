import pymysql
from decouple import config

#Get username from env
username = config("USER")
pw = config("PASS")

#Connect to DB
connection = pymysql.connect(host='localhost',
                            user=username,
                            password=pw,
                            db='Chinook')


try:
    #Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Friends;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    #Close the connection to the db
    connection.close()