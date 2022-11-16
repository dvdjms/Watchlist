
from flask import Blueprint, Flask, redirect, render_template, request

import repositories.director_repository as director_repository
from models.director import Director

directors_blueprint = Blueprint("directors", __name__)


# INDEX - DIRECTORS
@directors_blueprint.route("/directors")
def directors():
    # Call select_all function to get all director objects and render template
    directors = director_repository.select_all()
    return render_template("directors/index.html", directors=directors)


# VIEW DIRECTOR
@directors_blueprint.route("/directors/<id>")
def view_director(id):
    # Call select function to obtain director object by id and render template
    director = director_repository.select(id)
    return render_template("directors/director.html", director=director)


# ADD DIRECTOR
@directors_blueprint.route("/directors/add", methods=['GET', 'POST'])
def add_director():

    if request.method == 'GET':
        # Call select_all function to to all director objects and render template
        directors = director_repository.select_all()
        return render_template("directors/add.html", directors=directors)

    if request.method == 'POST':

        # Error checking
        directors = director_repository.select_all()
        # Check name has been entered - show message if not
        if request.form['name'] == "":
            return render_template("directors/add.html", directors=directors, message="Enter name")
        # Check nationality has been entered - show message if not
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
    # Call delete function to delete directors by id
    director_repository.delete_id(id)
    return redirect("/directors")


# EDIT DIRECTOR - LOAD WITH DIRECTOR DETAILS
@directors_blueprint.route("/directors/<id>/edit", methods=['POST'])
def edit_director(id):
    # Call select function to get director objects by id
    director = director_repository.select(id)
    return render_template("directors/edit.html", director=director)


# EDIT MOVIE - UPDATE BUTTON
@directors_blueprint.route("/directors/<id>", methods=['POST'])
def edit_director_update(id):
    # Call select function to get director objects by id
    director = director_repository.select(id)
    # Check name has been entered - show message if not
    if request.form['name'] == "":
        return render_template("directors/edit.html", director=director, message="Enter name")
    # Check nationality has been entered - show message if not
    if request.form['nationality'] == "":
        return render_template("directors/edit.html", director=director, message="Enter nationality")

    # Get user input
    name = request.form['name']
    nationality = request.form['nationality']
    # Put odirector bject into variable 
    director = Director(name, nationality, id)
    # Call update_direction function to amend director details
    director_repository.update_director(director)
    return redirect('/directors')



