# -*- coding: utf-8 -*-

from ex45 import *

Things={'name':'apple','applenum':'100','name2':'gold','goldnum':'10000'}

room1=Room1()
if room1.run()!="front":
	Death().others()	
else:
	room2=GoldRoom()
	room2.gold()
