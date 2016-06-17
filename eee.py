fo=open("words.txt","r+")
lines=fo.readlines()
dict1={}
for line in lines:
	sline=line.split(":")
	dict1[sline[0]]=sline[1]
	print dict1
