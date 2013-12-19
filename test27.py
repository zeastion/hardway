class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for a in self.lyrics:
			print a

happy_day = Song(["What a happy day",
		  "Play PSP",
		  "and iTouch"])

bulls_on_parade = Song(["They rally around the family",
			"With pockets full of shells"])

happy_day.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
