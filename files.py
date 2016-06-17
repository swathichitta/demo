#implementing file operations in newly created directory.
import os
obj=open("fun.txt","r+")
a=obj.tell()
print "current position of pointer in file is:",a
b=obj.read(20)
print "contents in file fun are:",b
c=obj.tell()
print "current position of pointer after read is:",c
obj.seek(0,0)
d=obj.read(20)
print d
obj.write("am writing contents to fun file")
obj.seek(0,0)
e=obj.read(40)
print e
os.rename("fun.txt","funy.txt")
print "name after renaming",file.name
obj.close()
print"file closed:",obj.closed

