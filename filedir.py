import os
a=os.getcwd();
print "curent working directory is",a
print "making a new directory."
os.mkdir("example directory");
print "changing directory to the new one"
os.chdir("example directory");
c=os.getcwd();
print "current directory",c

