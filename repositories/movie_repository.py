from db.run_sql import run_sql
from models.movie import Movie
from models.director import Director
import repositories.movie_repository as movie_repository
import repositories.director_repository as director_repository
# import repositories.user_repository as user_repository

def save(movie):
    sql = "INSERT INTO movies (title, genre, year, country, rating, watchlist, director_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [movie.title, movie.genre, movie.year, movie.country, movie.rating, movie.watchlist, movie.director.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    movie.id = id 


def select_all():
    movies = []
    sql = "SELECT * FROM movies ORDER BY id"
    results = run_sql(sql)
    for row in results:
        director = director_repository.select(row['director_id'])
        movie = Movie(row['title'], row['genre'], row['year'], row['country'], director, row['rating'], row['watchlist'], row['id'])
        movies.append(movie)
    return movies


def select_watchlist():
    movies = []
    sql = "SELECT * FROM movies WHERE watchlist = %s ORDER BY id"
    values = [True]
    results = run_sql(sql, values)
    for row in results:
        director = director_repository.select(row['director_id'])
        movie = Movie(row['title'], row['genre'], row['year'], row['country'], director, row['rating'], row['watchlist'], row['id'])
        movies.append(movie)
    return movies


def select(id):
    movie = None
    sql = "SELECT * FROM movies WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        director = director_repository.select(result['director_id'])
        movie = Movie(result['title'], result['genre'], result['year'], result['country'], director, result['rating'], result['watchlist'], result['id'])
    return movie


def delete_all():
    sql = "DELETE FROM movies"
    run_sql(sql)


def delete_id(id):
    sql = "DELETE FROM movies WHERE id = %s"
    values = [id]
    run_sql(sql, values)



def update_watchlist(id):
    movie = select(id)

    print(movie.title)
    print(movie.watchlist)

    if movie.watchlist == True:
        sql = "UPDATE movies SET watchlist = (%s) WHERE id = (%s)"
        values = [False, id]
        run_sql(sql, values)
    else:
        sql = "UPDATE movies SET watchlist = (%s) WHERE id = (%s)"
        values = [True, id]
        run_sql(sql, values)