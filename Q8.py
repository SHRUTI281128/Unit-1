class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def categorize(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Rating:", self.rating)
        print("Ticket Price: ₹", self.ticket_price)
        print("Category:", self.categorize())
        print("------------------------")


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\nMovie Collection")
        print("========================")

        for movie in self.movies:
            movie.display()


# Creating Cinema object
cinema = Cinema()

# Creating Movie objects
m1 = Movie("Avengers", 9, 250)
m2 = Movie("Dangal", 7, 200)
m3 = Movie("Race 3", 4, 150)

# Adding movies to cinema
cinema.add_movie(m1)
cinema.add_movie(m2)
cinema.add_movie(m3)

# Displaying movie details
cinema.display_movies()

'''
Movie Collection
========================
Movie Name: Avengers
Rating: 9
Ticket Price: ₹ 250
Category: Hit
------------------------
Movie Name: Dangal
Rating: 7
Ticket Price: ₹ 200
Category: Average
------------------------
Movie Name: Race 3
Rating: 4
Ticket Price: ₹ 150
Category: Flop
------------------------
'''
