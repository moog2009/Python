# -*- coding: utf-8 -*-

import ex45

Things={'name':'apple','applenum':'100','name2':'gold','goldnum':'10000'}

direction=['left','right','back','front']

room1=ex45.Room1()
room1.run(direction[3])

room2=ex45.GoldRoom()
room2.ecapse()
