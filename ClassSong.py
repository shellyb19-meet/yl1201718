lyrics = []
import random
class Song(object):
	"""docstring fos Song"""
	def __init__(self, lyrics):
		self.lyrics=lyrics

	def sing_me_a_song(self):
		for i in self.lyrics:
			print(random.choice(self.lyrics))
a= Song(["do yo", "po lo","haha"])
a.sing_me_a_song()
