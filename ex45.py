# -*- coding: utf-8 -*-

class GoldRoom(object):

	def __inif__(self):
		pass
		
	def gold(self):
		Things={'name':'apple','applenum':'100','name2':'gold coins','goldnum':'100'}
		print "You find 100 gold coins,how many coins you want to take?"
		num=int(raw_input())
		while True:
			if num>100:
				print "no more coins! please again!"
				num=raw_input()
			elif num>10 and num<=100:
				print "--"*10
				print "you died!hahaha~~~"
				exit(0)
			else:
				i=False
				print "you got %d %s!" %(num,Things['name2'])
				print "you win!"
				exit(0)
		
class Room1(object):
	
	def __inif__(self,things):
		self.things=things
	
	def getthings(things):
		print "you got %s!" %things
		return things
		
	def run(self):
		print "what do you do ?"
		print "press 1 : go right side."
		print "press 2 : go left side."
		print "press 3 : go back."
		print "press 4 : go front."
		direction=['left','right','back','front']
		s=int(raw_input())-1;
		print "you run %s." %direction[s]
		return direction[s]

class Death(object):
			
	def __inif__(self):
		pass
		
	def others(self):
		print "--"*10
		print "you died!hahaha~~~"
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		