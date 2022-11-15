
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


# ADD DIRECTOR
@directors_blueprint.route("/directors/add", methods=['GET', 'POST'])
def add_director():

    if request.method == 'GET':
        directors = director_repository.select_all()
        return render_template("directors/add.html", directors=directors)

    if request.method == 'POST':

        # Error checking
        directors = director_repository.select_all()
        if request.form['name'] == "":
            return render_template("directors/add.html", directors=directors, message="Enter name")
        if request.form['nationality'] == "":
            return render_template("directors/add.html", directors=directors, message="Enter nationality")


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


# EDIT DIRECTOR - LOAD WITH DIRECTOR DETAILS
@directors_blueprint.route("/directors/<id>/edit", methods=['POST'])
def edit_director(id):
    director = director_repository.select(id)
    return render_template("directors/edit.html", director=director)


# EDIT MOVIE - UPDATE BUTTON
@directors_blueprint.route("/directors/<id>", methods=['POST'])
def edit_director_update(id):
    name = request.form['name']
    nationality = request.form['nationality']
    director = Director(name, nationality, id)
    director_repository.update_director(director)
    return redirect('/directors')



