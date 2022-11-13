from db.run_sql import run_sql
from models.director import Director

def save(director):
    sql = "INSERT INTO directors (name) VALUES (%s) RETURNING *"
    values = [director.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    director.id = id


def delete_all():
    sql = "DELETE FROM directors"
    run_sql(sql)


def select_all():
    directors = []
    sql = "SELECT * FROM directors"
    results = run_sql(sql)
    for row in results:
        director = Director(row['name'], row['id'])
        directors.append(director)
    return directors


def select(id):
    director = None
    sql = "SELECT * FROM directors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        director = Director(result['name'], result['id'])
    return director


    