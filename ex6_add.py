# -*- coding: utf-8 -*-

#赋值字符变量x
x="There are %d types of people." %10
#赋值字符变量binary
binary="binary"
#赋值字符变量
do_not="don't" 
#赋值字符变量y （字符串包含字符串）
y="Those who know %s and those who %s." %(binary,do_not)

#打印变量X
print x
#打印变量y
print y

#打印含变量X的字符串 （字符串包含字符串）
print "I said: %r" %x
#打印含变量y的字符串 （字符串包含字符串）
print "I also said: '%s'." %y

#赋值字符变量hilarious
hilarious=True
#赋值字符变量joke_evaluation含字符串变量（字符串包含字符串）
joke_evaluation="Isn't that joke so funny?! %r"

#打印含变量joke_evaluation的字符串 （字符串包含字符串）
print joke_evaluation %hilarious

#赋值字符变量w
w="This is the left side of..."
#赋值字符变量e
e="a string with a right side."

##打印变量w+e。字符串拼接，类型相同，更长字符串。
print w+e
