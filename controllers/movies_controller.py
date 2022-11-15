from flask import Blueprint, Flask, redirect, render_template, request

import repositories.movie_repository as movie_repository
from models.movie import Movie
import repositories.director_repository as director_repository
from models.director import Director
import pdb

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
        print(directorid)
        title = request.form['title']
        genre = request.form['genre']
        year = request.form['year']
        country = request.form['country']
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
    movie_repository.delete_id(id)
    return redirect("/movies")


# UPDATE WATCHLIST FROM MOVIE PAGE - don't remove seen movies
@movies_blueprint.route("/movies/<id>/watch_status", methods=['POST'])
def update_watch1(id):
    movie_repository.update_watchlist(id)
    return redirect("/movies")


# UPDATE WATCHLIST FROM WATCHLIST PAGE - remove seen movies
@movies_blueprint.route("/watchlist/<id>/watch_status", methods=['POST'])
def update_watch2(id):
    movie_repository.update_watchlist(id)
    return redirect("/watchlist")


# EDIT MOVIE - LOAD WITH MOVIE DETAILS
@movies_blueprint.route("/movies/<id>/edit", methods=['POST'])
def edit_movie(id):
    directors = director_repository.select_all()
    movie = movie_repository.select(id)
    for director in directors:
        if movie.director.id == director.id:
            name = director.name
    id = movie.director.id
    return render_template("movies/edit.html", movie=movie, directors=directors, name=name, id=id)


# EDIT MOVIE - UPDATE BUTTON
@movies_blueprint.route("/movies/<id>", methods=['POST'])
def edit_movie_update(id):
    director1 = request.form['director']
    title = request.form['title']
    genre = request.form['genre']
    year = request.form['year']
    country = request.form['country']
    director = director_repository.select(director1)
    movie = Movie(title, genre, year, country, director, id=id)
    movie_repository.update_movie(movie)
    return redirect('/movies')










# def select_victims_of_zombie(id):
#     victims = []
#     sql = "SELECT humans.* FROM humans INNER JOIN bitings ON bitings.human_id = humans.id WHERE bitings.zombie_id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     for result in results:
#         human = Human(result["name"])
#         victims.append(human)
#     return victims

