def prnt(str):#exmpl 1
	print str
prnt("hello")
prnt("world")

def pbv(name,age):#exmpl 2
	Name=name
	Age=age
	print Name, Age
pbv("swathi",21)

def lst(mylist):#exmpl 3
	print mylist
lst([1,2,3,4,5,6,7,8,9,0])
xmpl=['a','b','c']
lst(xmpl)
lst({'a':1,'b':2,'c':3})

def ex(a,b):#exmpl 4
	print a,b
ex("hello","world")
ex(5,"times slower")

def rtn(m,n):#exmpl 5
	sum=m+n
	print sum	
	return sum
total=rtn(10,20)
total=rtn('a','b')

def mtd(str):#exmpl 6
	if len(str)<0:
		print "der exists no string"
	else:
		print str
mtd("hello world")
mtd(" ")

def md(str):#exmpl 6
	if len(str)<0:
		print str
	else:
		print "using pass stmt"
		pass
md("hello")


