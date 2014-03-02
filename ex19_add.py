# -*- coding: utf-8 -*-

#定义函数cheese_and_crackers
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" %cheese_count
	print "You have %d boxes_of_crackers!" %boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanker.\n"

#使用数字调用函数	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#使用变量调用函数
print "OR, We can user variables from our script:"
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#调用函数的参数使用表达式
print "We can even do much inside too:"
cheese_and_crackers(10+20,5+6)

#调用函数的参数使用含参数的表达式
print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese+10,amount_of_crackers+1000)
