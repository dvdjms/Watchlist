from flask import Flask, render_template

from controllers.movies_controller import movies_blueprint
from controllers.directors_controller import directors_blueprint


app = Flask(__name__)

app.register_blueprint(movies_blueprint)
app.register_blueprint(directors_blueprint)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()