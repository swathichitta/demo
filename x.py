fo = open("fun.txt", "r+")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
str = fo.read(10);
print "Read String is : ", str
position = fo.tell();
print "current position",position
position = fo.seek(0, 0);
print "position now",position

