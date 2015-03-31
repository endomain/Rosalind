#Enumerating Gene Orders
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/perm
"""

n = int(raw_input())

l=[]
for i in range(1,n+1):
	l.append(i)

import itertools
a = list(itertools.permutations(l))

print " "
print len(a)

for x in a:
	for i in range(0,n):
		print x[i],
	print " "