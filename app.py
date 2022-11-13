from flask import Flask, render_template

from controllers.users_controller import users_blueprint
from controllers.movies_controller import movies_blueprint
from controllers.directors_controller import directors_blueprint
# from controllers.watchlist_controller import watchlist_blueprint



app = Flask(__name__)

app.register_blueprint(users_blueprint)
app.register_blueprint(movies_blueprint)
app.register_blueprint(directors_blueprint)
# app.register_blueprint(watchlist_blueprint)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()