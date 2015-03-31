#Enumerating k-mers Lexicographically

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/lexf
"""

s = str(raw_input())
n = int(raw_input())

letters = s.split(' ')

lista = []
listb = []

for i in range(0,len(letters)): 
	lista.append(i)

import itertools
listb = list(itertools.product(lista,repeat = n))

import sys
for item in listb:
	k = []
	for i in item:
		k.append(letters[i])
	print "".join(k)
