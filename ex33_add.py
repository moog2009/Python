# -*- coding: utf-8 -*-
def Add(endnum):
	i=0
	numbers=[]

	while i<endnum:
		print "At the top i is %d" %i
		numbers.append(i)
		
		i=i+1
		print "Numbers now:",numbers
		print "At the bottom i is %d" %i
		
	print "The numbers:"

	for num in numbers:
		print num
	return numbers
	
endnum=3
numbers=[]
numbers=Add(endnum)
numbers.append(9)
print "-"*12
for i in numbers:
	print "%s" %i