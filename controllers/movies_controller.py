from flask import Blueprint, Flask, redirect, render_template, request

import repositories.movie_repository as movie_repository
from models.movie import Movie
import repositories.director_repository as director_repository
from models.director import Director

movies_blueprint = Blueprint("movies", __name__)

# INDEX - MOVIES
@movies_blueprint.route("/movies")
def movies():
    movies = movie_repository.select_all()
    return render_template("movies/index.html", movies=movies)


# VIEW INDIVIDUAL MOVIE
@movies_blueprint.route("/movies/<id>")
def view_movie(id):
    movie = movie_repository.select(id)
    return render_template("movies/movie.html", movie=movie)


# VIEW WATCHLIST
@movies_blueprint.route("/watchlist")
def view_movie_watchlist():
    movies = movie_repository.select_watchlist()
    return render_template("watchlist/index.html", movies=movies)


# ADD MOVIE
@movies_blueprint.route("/movies/add", methods=['GET', 'POST'])
def add_movie():

    if request.method == 'GET':
        directors = director_repository.select_all()
        return render_template("movies/add.html", directors=directors)

    if request.method == 'POST':
        # Get information posted by user
        directorid = request.form['director']
        title = request.form['title']
        genre = request.form['genre']
        year = request.form['year']
        country = request.form['country']
        rating = 0
        watchlist = True
        # Get director's information from director id
        directors = director_repository.select(directorid)
        # Save to variable
        movie = Movie(title, directors, genre, year, country, rating, watchlist, directors)
        # Save new movie entry
        movie_repository.save(movie)
        return redirect('/movies')




