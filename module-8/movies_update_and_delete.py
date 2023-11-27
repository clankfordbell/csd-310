import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "admin",
    "host": "",
    "database": "movies",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()


def show_films(cursor, title):

    cursor.execute(
        "select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    results = cursor.fetchall()

    print("\n -- {} --".format(title))

    for row in results:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(row[0], row[1], row[2], row[3]))


show_films(cursor, "DISPLAYING FILMS AFTER DELETE")




