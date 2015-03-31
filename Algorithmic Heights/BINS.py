#Binary Search
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/bins
"""

f = open(raw_input("Type your input file name exactly: "), 'r')
lines = f.readlines()
f.close()

n = int(lines[0])
m = int(lines[1])
A = lines[2].split(" ")
B = lines[3].split(" ")

for x in B:
	if x in A:
		b = A.index(x) + 1
		print b, 
	else:
		print "-1",
