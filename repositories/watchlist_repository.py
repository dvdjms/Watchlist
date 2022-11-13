from db.run_sql import run_sql
from models.movie import Movie
from models.director import Director
from models.watchlist import Watchlist
import repositories.movie_repository as movie_repository
import repositories.director_repository as director_repository
import repositories.watchlist_repository as watchlist_repository

# def save(watchlist):
#     sql = "INSERT INTO watchlist (user_id, movie_id) VALUES (%s, %s) RETURNING *"
#     values = [watchlist.user_id.id, watchlist.movie_id.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     watchlist.id = id 


# def select_all():
#     watchlistdic = []
#     # sql = "SELECT * FROM movies"
#     # movie_results = run_sql(sql)
#     sql = "SELECT * FROM movies"
#     results = run_sql(sql)

#     for row in results:
#         # for row in watchlist_results[row]:
#         watch = Watchlist(row['user_id'], row['movie_id'], row[0])
#         print(watch)
#         movie = Movie(row['title'], row['director'], row['genre'], row['year'], row['rating'], watch)
#         watchlistdic.append(movie)
      
    
        # if movie_results[row]['id'] in watchlist_results[row]['movie_id']:

        #     movie = Movie(row['title'], row['director'], row['genre'], row['year'], row['rating'], row['id'])
        #     watchlistdic.append(movie)
    # return watchlistdic

        # movies.append(movie)
# def select_all():
#     movies = []
#     sql = "SELECT * FROM movies"
#     results = run_sql(sql)
#     for row in results:
#         movie = Movie(row['title'], row['director'], row['genre'], row['year'], row['rating'], row['id'])
#         movies.append(movie)
#     return movies



# def delete_all():
#     sql = "DELETE FROM watchlist"
#     run_sql(sql)


# def select(id):
#     watchlist = None
#     sql = "SELECT * FROM watchlist WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     if results:
#         result = results[0]
#         watchlist = Watchlist(result['user_id'], result['movie_id'], result['id'])
#     return watchlist

