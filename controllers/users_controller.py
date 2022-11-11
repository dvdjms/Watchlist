from flask import Blueprint, Flask, redirect, render_template, request
import repositories.user_repository as user_repository
import repositories.movie_repository as movie_repository
import repositories.director_repository as director_repository
from models.user import User

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)



