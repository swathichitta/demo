print 'hello'
a={'abc':'a','pqr':1,5:9,9:'d','mnc':'sdf'}
n={'abc':'a','pqr':1,5:9,9:'d','mnc':'sdf'}
b={'a':1,2:'b','and':'sss','j':'k',0:0}

#printing values with respect to keys
print a
print a['abc']
print a['pqr']
print a[5]
print a[9]
print a['mnc']
#built_in functions
print cmp(a,n)#true 0
print cmp(a,b)#false 1
print len(a)#no of elements of a
print len(b)#no of elements of b
print str(a)#prints dict a
print str(b)#prints dict b
print type(a)#dict
#built_in methods
a.clear()
print a#clears all elements from dict a
z=n.copy()
print z#copies elements of n to z
print n.fromkeys('abcdyfshgvjkhdkjhuk')#makes each char as a key 
print n.fromkeys(b)#takes keys of dict b
print b.get(0,None)
print b.has_key('a')#returns true if it has a key 'a'
print b.items()#puts pairs of key and values
print b.setdefault('f',9)
print b
print n
print b.update(n)#adds n key value pairs to b
print b
print n
print b.values()#prints values of dict b
print b.keys()#prints keys of dict b
print b.get('a')#returns the value of key a if exists

