# -*- coding: utf-8 -*-

#引入变量argv
from sys import argv
#通过键盘输入将值赋予变量input_file
script,input_file=argv
#定义函数print_all：打印f内的信息
def print_all(f):
	print f.read()
#重置打开文档的位置	
def rewind(f):
	f.seek(0)
#打印某行信息
def print_a_line(line_count,f):
	print line_count,f.readline()
#打开文件input_file
current_file=open(input_file)

print "First let's print the whole file:\n"
#打印打开的文件内的信息
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#调用重置
rewind(current_file)

print "Let's print three lines:"
#打印第1、2、3行信息
curent_line=1
print_a_line(curent_line,current_file)

curent_line+=1
print_a_line(curent_line,current_file)

curent_line+=1
print_a_line(curent_line,current_file)
