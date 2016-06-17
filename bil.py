name=raw_input("name :")
meter_no=raw_input("meter_no :")
units=int(raw_input("units consumed :"))
print "\nDear",name
print "your meter no is",meter_no
print "your consumed units are",units
if (units<100):
	print "your total bill is:",(units*10)
elif (units>100 & units<200):
	print "your total bill is:",((100*10)+((units-100)*12))
elif (units>200 & units<300):
	print "your total bill is:",((100*10)+(100*12)+((units-200)*15))
elif (units>300 & units<400):
	print "your total bill is:",((100*10)+(100*12)+(100*15)+((units-300)*20))
elif (units>400 & units<500):
	print "your total bill is:",((100*10)+(100*12)+(100*15)+(100*20)+((units-400)*25))
elif (units>500 & units<1000):
	print "your total bill is:",((100*10)+(100*12)+(100*15)+(100*20)+(100*25)+((units-500)*30))		
elif (units>1000):
	print "your total bill is:",((100*10)+(100*12)+(100*15)+(100*20)+(100*25)+(100*30)+((units-600)*40))
else:
	pass
	