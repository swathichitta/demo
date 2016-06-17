fo=open("words.txt","r+")
word=raw_input("enter your word:")
lines=fo.readlines()
dictionary={}
for line in lines:
	sline = line.split(':')
	dictionary[sline[0]] = sline[1]

if word in dictionary.keys():
	print dictionary[word]
else:
	print "word not found"