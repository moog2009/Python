# -*- coding: utf-8 -*-

from ex45 import *

room1=Room1()
if room1.run()!="front":
	Death().others()	
else:
	room2=GoldRoom()
	room2.gold()
