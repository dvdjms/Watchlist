-- DROP TABLE IF EXISTS watchlist;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS directors;


CREATE TABLE directors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    nationality VARCHAR(255)
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    country VARCHAR(255) NOT NULL,
    rating INT NOT NULL,
    watchlist BOOLEAN NOT NULL,
    director_id INT NOT NULL REFERENCES directors(id) ON DELETE CASCADE
);



