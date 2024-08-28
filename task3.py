import pymysql

# Connect to the database
connection = pymysql.connect(   
    host = '127.0.0.1',
    user = 'root',
    password= '12345',
    db='Movie_info',
    port = 3306,
    charset = 'utf8mb4', 
    cursorclass= pymysql.cursors.DictCursor
)
print(connection.host_info)
