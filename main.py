import requests
from task3 import connection

def get_movie_data(title):
    api_key = '5d9df2b8'
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if data['Response'] == 'True':
        my_dict = {}
        title = data.get('Title', 'N/A')
        released = data.get('Released', 'N/A')
        genre = data.get('Genre', 'N/A')
        director = data.get('Director', 'N/A')

        my_dict['title'] = title
        my_dict['released'] = released
        my_dict['genre'] = genre
        my_dict['director'] = director



        
        print(f"Title: {title}")
        print(f"Released: {released}")
        print(f"Genre: {genre}")
        print(f"Director: {director}")

        return my_dict
    else:
        print("The movie does not exist in the database.")

# insert data into the table
def insert_into_blog(title, director, released, genre):
    print(title)
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Movie_info.Movie_info (Title, released, director, genre) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (title, released, director, genre))
        connection.commit()

# Example usage
mymovie = input("Kinonun adini daxil edin: ")
print(get_movie_data(mymovie))

insert_into_blog(get_movie_data(mymovie)['title'],get_movie_data(mymovie)['released'],
                 get_movie_data(mymovie)['director'], get_movie_data(mymovie)['genre'])

 
