from flask import Blueprint, Flask, redirect, render_template, request

import repositories.movie_repository as movie_repository
from models.movie import Movie
import repositories.director_repository as director_repository


movies_blueprint = Blueprint("movies", __name__)

# INDEX - MOVIES
@movies_blueprint.route("/movies")
def movies():
    # Call select_all function to to all movie objects and render template
    movies = movie_repository.select_all()
    return render_template("movies/index.html", movies=movies)


# VIEW INDIVIDUAL MOVIE
@movies_blueprint.route("/movies/<id>")
def view_movie(id):
    # Call select function to obtain movie object by id and render template
    movie = movie_repository.select(id)
    return render_template("movies/movie.html", movie=movie)


# VIEW WATCHLIST
@movies_blueprint.route("/watchlist")
def view_movie_watchlist():
    # Call select
    movies = movie_repository.select_watchlist()
    return render_template("watchlist/index.html", movies=movies)


# ADD MOVIE
@movies_blueprint.route("/movies/add", methods=['GET', 'POST'])
def add_movie():

    if request.method == 'GET':
        # Call select all directors function and render template
        directors = director_repository.select_all()
        return render_template("movies/add.html", directors=directors)

    if request.method == 'POST':

        # Error checking
        directors = director_repository.select_all()
        if request.form['director'] == 'Director':
            return render_template("movies/add.html", directors=directors, message="Enter director")
        if request.form['title'] == "":
            return render_template("movies/add.html", directors=directors, message="Enter title")
        if request.form['genre'] == 'Genre':
            return render_template("movies/add.html", directors=directors, message="Enter genre")
        if request.form['year'] == 'Year':
            return render_template("movies/add.html", directors=directors, message="Enter year")
        if request.form['country'] == 'Country':
            return render_template("movies/add.html", directors=directors, message="Enter country")

        # Get information posted by user
        directorid = request.form['director']
        title = request.form['title']
        genre = request.form['genre']
        year = request.form['year']
        country = request.form['country']
        # Hard code rating and watchlist values
        rating = 0
        watchlist = True
        # Get director's information from director id
        directors = director_repository.select(directorid)
        # Save to variable
        movie = Movie(title, genre, year, country, directors, rating, watchlist)
        # Save new movie entry
        movie_repository.save(movie)
        return redirect('/movies')


# DELETE MOVIE
@movies_blueprint.route("/movies/<id>/delete", methods=['POST'])
def delete_movie(id):
    # Call delete by id movie function
    movie_repository.delete_id(id)
    return redirect("/movies")


# UPDATE WATCHLIST FROM MOVIE PAGE - don't remove seen movies
@movies_blueprint.route("/movies/<id>/watch_status", methods=['POST'])
def update_watch1(id):
    # Call update_watchlist function via movie page - boolean
    movie_repository.update_watchlist(id)
    return redirect("/movies")


# UPDATE WATCHLIST FROM WATCHLIST PAGE - remove seen movies
@movies_blueprint.route("/watchlist/<id>/watch_status", methods=['POST'])
def update_watch2(id):
    # Call update_watchlist function via watchlist page - boolean
    movie_repository.update_watchlist(id)
    return redirect("/watchlist")


# EDIT MOVIE - LOAD WITH MOVIE DETAILS
@movies_blueprint.route("/movies/<id>/edit", methods=['POST'])
def edit_movie(id):
    # Call select_all function
    directors = director_repository.select_all()
    # Get movie object by id
    movie = movie_repository.select(id)
    # Iterate over directors
    for director in directors:
        # Look for a match between id and foreign id
        if movie.director.id == director.id:
            # Save name into variable
            name = director.name
    # Get director id/foreign key
    id = movie.director.id
    return render_template("movies/edit.html", movie=movie, directors=directors, name=name, id=id)


# EDIT MOVIE - UPDATE BUTTON
@movies_blueprint.route("/movies/<id>/update", methods=['POST'])
def edit_movie_update(id):
    # Obtained information from user
    directorid = request.form['director']
    title = request.form['title']
    genre = request.form['genre']
    year = request.form['year']
    country = request.form['country']
    # Get director object
    director = director_repository.select(directorid)
    movie = Movie(title, genre, year, country, director, id=id)
    # Call update_movie function
    movie_repository.update_movie(movie)
    return redirect('/movies')


# UPDATE MOVIE RATING
@movies_blueprint.route("/movies/<id>/rating", methods=['POST'])
def update_movie_rating(id):
    # Obtain user rating
    rating = request.form['rating']
    # Get movie oject by id
    movie_ = movie_repository.select(id)
    movie = Movie(movie_.title, movie_.genre, movie_.year, movie_.country, movie_.director, rating, id=id)
    # Call update_rating function
    movie_repository.update_rating(movie)
    return redirect('/movies')

