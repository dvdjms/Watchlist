from db.run_sql import run_sql
from models.movie import Movie
from models.director import Director
import repositories.movie_repository as movie_repository
import repositories.director_repository as director_repository
# import repositories.user_repository as user_repository

def save(movie):
    sql = "INSERT INTO movies (title, director, genre, year, country, rating, watchlist, director_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [movie.title, movie.director.name, movie.genre, movie.year, movie.country, movie.rating, movie.watchlist, movie.director.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    movie.id = id 


def select_all():
    movies = []
    sql = "SELECT * FROM movies"
    results = run_sql(sql)
    for row in results:
        movie = Movie(row['title'], row['director'], row['genre'], row['year'], row['country'], row['rating'], row['watchlist'], row['id'])
        movies.append(movie)
    return movies


def select_watchlist():
    movies = []
    sql = "SELECT * FROM movies WHERE watchlist = %s"
    values = [True]
    results = run_sql(sql, values)
    for row in results:
        movie = Movie(row['title'], row['director'], row['genre'], row['year'], row['country'], row['rating'], row['watchlist'], row['id'])
        movies.append(movie)
    return movies


def delete_all():
    sql = "DELETE FROM movies"
    run_sql(sql)


def select(id):
    movie = None
    sql = "SELECT * FROM movies WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        movie = Movie(result['title'], result['director'], result['genre'], result['year'], result['rating'], result['watchlist'], result['id'])
    return movie







