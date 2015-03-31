#Majority Element
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/maj
"""


f = open(raw_input("Type your input file name exactly: "), 'r')
lines = f.readlines()
f.close()

num = lines[0].split(" ")
k = int(num[0])
n = int(num[1])
m = n/2
array = []

for x in range(1,k+1):
	lines[x] = lines[x].replace("\n", "")
	y = lines[x].split(" ")
	y = map(int, y)
	array.append(y)

from collections import Counter

for h in range(0,k):
	i = array[h]
	l = Counter(array[h])
	allvalues = l.values()
	if all(number <= m for number in allvalues):
		print "-1",
	else:
		for key, value in l.iteritems():
			if value > m:
				print key,
	

