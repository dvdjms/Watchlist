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


    