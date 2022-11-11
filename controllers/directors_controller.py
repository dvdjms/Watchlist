
from flask import Blueprint, Flask, redirect, render_template, request

import repositories.director_repository as director_repository
from models.director import Director

directors_blueprint = Blueprint("directors", __name__)

# INDEX
@directors_blueprint.route("/directors")
def directors():
    directors = director_repository.select_all()
    return render_template("directors/index.html", directors=directors)


