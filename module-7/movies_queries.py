import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "admin",
    "host": "",
    "database": "movies",
    "raise_on_warnings": True
}


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    print("-- DISPLAYING Studio RECORDS --")
    cursor = db.cursor()
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    results = cursor.fetchall()
    for rows in results:
        print("Studio ID: {}\nStudio Name:{}\n".format(rows[0], rows[1]))
    print("-- DISPLAYING Genre RECORDS --")
    cursor = db.cursor()
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    results = cursor.fetchall()
    for rows in results:
        print("Genre ID: {}\nGenre Name: {}".format(rows[0], rows[1]))
        print()
    print("-- DISPLAYING Short Film RECORDS --")
    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    results = cursor.fetchall()
    for rows in results:
        print("Film Name: {}\nRuntime: {}".format(rows[0], rows[1]))
        print()
    print("-- DISPLAYING Director RECORDS in Order --")
    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    results = cursor.fetchall()
    for rows in results:
        print("Film Name: {}\nDirector: {}".format(rows[0], rows[1]))
        print()

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied user or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()