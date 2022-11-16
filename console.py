import pdb

from models.movie import Movie
import repositories.movie_repository as movie_repository

from models.director import Director
import repositories.director_repository as director_repository


movie_repository.delete_all()
director_repository.delete_all()


director_1 = Director("Martin Scorsese", "United States")
director_repository.save(director_1)

director_2 = Director("Quentin Tarantino", "United States")
director_repository.save(director_2)

director_3 = Director("Robert Zemekis", "United States")
director_repository.save(director_3)

director_4= Director("Wim Wenders", "German")
director_repository.save(director_4)

director_5 = Director("Joel Schumacher", "United States")
director_repository.save(director_5)

director_6 = Director("Steven Spielberg", "United States")
director_repository.save(director_6)


movie_1 = Movie("Paris, Texas", "Drama", 1984, "Germany", director_4, 9, True)
movie_repository.save(movie_1)

movie_2 = Movie("ET: Extra Terrestrial", "Science Fiction", 1982, "United States", director_6, 8, False)
movie_repository.save(movie_2)

movie_3 = Movie("Back to the Future", "Science Fiction", 1985, "United States", director_3, 8, False)
movie_repository.save(movie_3)

movie_4 = Movie("The Lost Boys", "Fantasy", 1987, "United States", director_5, 6, True)
movie_repository.save(movie_4)

movie_5 = Movie("Romance in the Stone", "Comedy, Romance", 1984, "United States", director_3, 7, True)
movie_repository.save(movie_5)

# watchlist_1 = Watchlist(user_1, movie_4, director_5)
# watchlist_repository.save(watchlist_1)

# watchlist_1 = Watchlist(user_1, movie_5, director_3)
# watchlist_repository.save(watchlist_1)

# watchlist_2 = Watchlist(user_2, movie_5, director_3)
# watchlist_repository.save(watchlist_2)

pdb.set_trace()