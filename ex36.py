# -*- coding: utf-8 -*-

from sys import exit
		
def bear_room(honeystatus):
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved=False
	
	if honeystatus == 1:
		while True:
			next=raw_input(">")		
			if next=="throw honey" and not bear_moved:
				print "The bear has moved from the door. You can go though is now."
				bear_moved=True
				honeystatus=0
			elif next =="back":
				first_room()
			elif next =="open door" and bear_moved:
				gold_room()
			elif next =="open door" and not bear_moved:
				dead("The bear gets pissed off and chews your head off.")
			else:
				print "I got no idea what that means."
	else:
		while True:
			next=raw_input(">")		
			if next =="back":
				first_room(0,0)
			elif next =="open door" and not bear_moved:
				dead("The bear gets pissed off and chews your head off.")
			elif next=="throw honey":
				print "I have no honey"
			else:
				print "I got no idea what that means."
				
				
def empty_room():
	print "There is a empty room."
	print "there are only a honey,what do you do?"
	honeystatus=0
	while True:
		next=raw_input(">")		
		if next =="back":
			first_room(0,honeystatus)
		elif next =="pick up the honey":
			honeystatus=1
			print "You pick up the honey, and what do you do now?"
		else:
			print "I got no idea what that means."
	
			
def first_room(x,y):
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"	
	honeystatus=y	
	next=raw_input(">")
	if next=="left":
		empty_room()
	elif next =="right":
		bear_room(honeystatus)
	else:
		dead("You stumble around the room until you starve.")			
				
def gold_room():
	print "This room is lots of gold and girls. How much do you take?"
	
	next=raw_input(">")
	if "0" in next or "1" in next:
		how_much=int(next)
	else:
		dead("man,learn to type a number.")
		
	if how_much<50:
		print "Nice, you're not greedy,you win!"
		exit(0)
	else:
		dead("You greedy bastard! you lose")
		
def dead(why):
	print why, "Good job!"
	exit(0)

		
man=0
honey=0		
first_room(man,honey)				
				
				
				
				
				
				
				
				
				
				
				
				