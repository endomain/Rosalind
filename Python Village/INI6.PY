#Dictionaries 

file1 = open(raw_input("Type your input file name exactly: "), 'r')
lines = file1.readlines()
file1.close()

s = str(lines)
l = s[2:len(s)-2]

allw = l.split(' ')

from collections import Counter

k = Counter(allw)

for key, value in k.items():
	print key 
	print value
