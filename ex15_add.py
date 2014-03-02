# -*- coding: utf-8 -*-

#引入参数变量argv
from sys import argv

#设置参数的名称数量
script,filename=argv
#打开filename的文件
txt=open(filename)
#打印信息
print "Here's your file %r:" %filename
#打印文件内的信息
print txt.read(2)
#关闭文件
txt.close()


