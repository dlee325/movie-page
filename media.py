# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie(): # Example of a class.
	""" This class provides a way to store movie related information"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): # '__init__' is an example of a constructor. 'self' is the actual object created.
		self.title = movie_title # Example of an instance variable.
		self.storyline = movie_storyline  # Example of an instance variable.
		self.poster_image_url = poster_image # Example of an instance variable.
		self.trailer_youtube_url = trailer_youtube # Example of an instance variable.

	def show_trailer(self): # Example of an instance method.
		webbrowser.open(self.trailer_youtube_url)

