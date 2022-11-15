from db.run_sql import run_sql
from models.director import Director

def save(director):
    sql = "INSERT INTO directors (name, nationality) VALUES (%s, %s) RETURNING *"
    values = [director.name, director.nationality]
    results = run_sql(sql, values)
    id = results[0]['id']
    director.id = id


def select_all():
    directors = []
    sql = "SELECT * FROM directors"
    results = run_sql(sql)
    for row in results:
        director = Director(row['name'], row['nationality'], row['id'])
        directors.append(director)
    return directors


def select(id):
    director = None
    sql = "SELECT * FROM directors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        director = Director(result['name'], result['nationality'], result['id'])
    return director


def delete_all():
    sql = "DELETE FROM directors"
    run_sql(sql)


def delete_id(id):
    sql = "DELETE FROM directors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update_director(director):
    sql = "UPDATE directors SET (name, nationality) = (%s, %s) WHERE id = (%s) RETURNING *"
    values = [director.name, director.nationality, director.id]
    run_sql(sql, values) 