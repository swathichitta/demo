print "please enter your details"
print "\n name:"
a=raw_input(str)
print "meter number:"
b=raw_input(int)
print "units consumed:"
c=raw_input(int)
summ=0
if c in (1000,10000):
	x=c-1000
	summ=summ+(x*50)
	c=1000
elif c in (500,1000):
	y=c-500
	summ=summ+(y*30)
	c=500
elif c in (400,500):
	z=c-400
	summ=summ+(z*20)
	c=400
elif c in (300,400):
	p=c-300
	summ=summ+(p*15)
	c=300
elif c in (200,300):
	q=b-200
	summ=summ+(q*12)
	c=200
elif c in (100,200):
	r=c-100
	summ=summ+(r*10)
	c=100
elif c==100:
	
	summ=summ+(c*10)
	
elif c<100:
	summ=summ+(c*5)
	total=summ
else:
	pass
print total

