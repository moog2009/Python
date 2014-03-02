# -*- coding: utf-8 -*-

class Song(object):

	def __init__(self,lyrics):
		self.lyrics=lyrics
		print lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday=Song(["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there",
				"New lyrics!"])
				
bulls_on_parade=Song(["They rally around the family",
					"With pockets full of shells"])
					
new_lyrics=Song(["OOOOOOOOOOOO",
				"XXXXXXXXXXXXX"])
					
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

new_lyrics.sing_me_a_song()

new_lyrics.__init__('1111')
