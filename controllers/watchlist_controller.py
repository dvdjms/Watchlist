from flask import Blueprint, Flask, redirect, render_template, request

import repositories.watchlist_repository as watchlist_repository
import repositories.movie_repository as movies_repository
import repositories.director_repository as directors_repository
import repositories.user_repository as users_repository
from models.watchlist import Watchlist
from models.movie import Movie
from models.user import User

# watchlist_blueprint = Blueprint("watchlist", __name__)

# # INDEX - MOVIES
# @watchlist_blueprint.route("/watchlist")
# def watchlist():
#     movies = watchlist_repository.select_all()
#     return render_template("movies/index.html", movies=movies)


# @watchlist_blueprint.route("/watchlist")
# def watchlist():
#     movies = []
#     watchlist = watchlist_repository.select_all()
#     movies = movies_repository.select(id)
#     for w in watchlist:
#         print(w)
#         if  == watchlist['user_id']:
#             # print(user)
#             print(w.user_id)
#             films = movies_repository.select(user)
#             movies.append(films)

#     return render_template("watchlist/index.html", watchlist=watchlist, movies=movies)


# VIEW MOVIES
# @watchlist_blueprint.route("/movies/<id>")
# def view_movie_watchlist(id):
#     watchlist = watchlist_repository.select(id)
#     movies = movies_repository.select(id)
#     return render_template("movies/movie.html", watchlist=watchlist, movies=movies)



# @movies_blueprint.route("/movies/<id>/view")
# def view_(id):
#     movies = movie_repository.select(id)
#     return render_template('movies/view.html', movies=movies)

