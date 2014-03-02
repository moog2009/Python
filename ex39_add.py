# -*- coding: utf-8 -*-

stuff={'name':'Zed','age':'36','height':'6*12+2'}

for (x,y) in stuff.items():
	print "%s:" %x,y
print "-"*15	
for x in stuff:
	print "%s:" %x,stuff[x]	
print "-"*15		
print stuff.items()
print stuff