# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script,from_file,to_file=argv

#we could do these two on one line too,how?
#indata=open(from_file).read()

open(to_file,'w').write("copy:"+open(from_file).read())



