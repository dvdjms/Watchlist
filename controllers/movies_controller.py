from flask import Blueprint, Flask, redirect, render_template, request

import repositories.movie_repository as movie_repository
from models.movie import Movie

movies_blueprint = Blueprint("movies", __name__)

# INDEX
@movies_blueprint.route("/movies")
def movies():
    movies = movie_repository.select_all()
    return render_template("movies/index.html", movies=movies)


# VIEW
@movies_blueprint.route("/movies/<id>")
def view_movie(id):
    print(id)
    movie = movie_repository.select(id)
    print(movie)
    return render_template("movies/view.html", movie=movie)



# @movies_blueprint.route("/movies/<id>/view")
# def view_(id):
#     movies = movie_repository.select(id)
#     return render_template('movies/view.html', movies=movies)

