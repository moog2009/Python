# -*- coding: utf-8 -*-

from sys import argv

script,filename=argv

print "We're going to erase %r." %filename
print "If you don't what that,hit CTRL-C(^c)."
print "If you do want that hit RETURN."

raw_input("--->")

print "Opening the file..."
target=open(filename,'w')

print "Truncating the file . Goodbye!"
target.truncate

print "Now I'm going to ask you for three lines."

line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "And finally, We close it."
target.close()