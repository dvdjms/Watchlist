
from flask import Blueprint, Flask, redirect, render_template, request

import repositories.director_repository as director_repository
from models.director import Director

directors_blueprint = Blueprint("directors", __name__)


# INDEX - DIRECTORS
@directors_blueprint.route("/directors")
def directors():
    directors = director_repository.select_all()
    return render_template("directors/index.html", directors=directors)


# VIEW DIRECTOR
@directors_blueprint.route("/directors/<id>")
def view_director(id):
    print(id)
    director = director_repository.select(id)
    return render_template("directors/director.html", director=director)


# ADD MOVIE
@directors_blueprint.route("/directors/add", methods=['GET', 'POST'])
def add_director():

    if request.method == 'GET':
        directors = director_repository.select_all()
        return render_template("directors/add.html", directors=directors)

    if request.method == 'POST':
        # Get information posted by user
        name = request.form['name']
        nationality = request.form['nationality']
   
        # Save to variable
        directors = Director(name, nationality)
        # Save new movie entry
        director_repository.save(directors)
        return redirect('/directors')


# DELETE MOVIE
@directors_blueprint.route("/directors/<id>/delete", methods=['POST'])
def delete_director(id):
    director_repository.delete_id(id)
    return redirect("/directors")

