import pdb

from models.user import User
import repositories.user_repository as user_repository

from models.movie import Movie
import repositories.movie_repository as movie_repository

from models.director import Director
import repositories.director_repository as director_repository


user_repository.delete_all()
movie_repository.delete_all()
director_repository.delete_all()


user_1 = User("John", "Johnson")
user_repository.save(user_1)

user_2 = User("Sam", "Samson")
user_repository.save(user_2)

user_3 = User("Robert", "Robertson")
user_repository.save(user_3)

user_4 = User("Eric", "Ericson")
user_repository.save(user_4)

director_1 = Director("Martin Scorsese")
director_repository.save(director_1)

director_2 = Director("Quentin Tarantino")
director_repository.save(director_2)

director_3 = Director("Robert Zemekis")
director_repository.save(director_3)

director_4= Director("Wim Wenders")
director_repository.save(director_4)

director_5 = Director("Joel Schumacher")
director_repository.save(director_5)

director_6 = Director("Steven Speilberg")
director_repository.save(director_6)


movie_1 = Movie("Paris, Texas", director_4, "Drama", 1984, 10)
movie_repository.save(movie_1)

movie_2 = Movie("ET: Extra Terrestrial", director_6, "Science Fiction", 1982, 8)
movie_repository.save(movie_2)

movie_3 = Movie("Back to the Future", director_3, "Science Fiction", 1985, 8)
movie_repository.save(movie_3)

movie_4 = Movie("The Lost Boys", director_5, "Fantasy", 1987, 6)
movie_repository.save(movie_4)

movie_5 = Movie("Romance in the Stone", director_3, "Comedy, Romance", 1984, 7)
movie_repository.save(movie_5)



pdb.set_trace()