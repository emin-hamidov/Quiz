import task3

    connection = task3.connect(
        host='127.0.0.1',  
        user='root',  
        password='12345', 
        db='Movie_info', 
        port = 3306,
        charset = 'utf8mb4', 
        cursorclass= task3.cursors.DictCursor
    )