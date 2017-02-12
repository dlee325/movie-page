# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import fresh_tomatoes # Imports the webpage template.
import media # Imports the class definition file to be used here.

toy_story = media.Movie("Toy Story", # Example of an instance of a class
						"A story of a boy and his toys that come to file",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", # Example of an instance of a class
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=-9ceBgWV8io")

dumb_and_dumber = media.Movie("Dumb and Dumber", # Example of an instance of a class
							  "Two friends return a briefcase to its owner",
							  "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
							  "https://www.youtube.com/watch?v=Knzdsr4OsXA")

midnight_in_paris = media.Movie("Midnight in Paris", # Example of an instance of a class
							  "Going back in time to meet authors",
							  "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
							  "https://www.youtube.com/watch?v=FAfR8omt-CY")

lost_in_translation = media.Movie("Lost in Translation", # Example of an instance of a class
							  "Two strangers befriend each other in Japan",
							  "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",
							  "https://www.youtube.com/watch?v=C4wCIiwa6DU")

inception = media.Movie("Inception", # Example of an instance of a class
							  "Professional thieves steals informtion by infiltrating the subconscious of others",
							  "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
							  "https://www.youtube.com/watch?v=8hP9D6kZseM")


movies = [toy_story, avatar, dumb_and_dumber, midnight_in_paris, lost_in_translation, inception]

fresh_tomatoes.open_movies_page(movies)
