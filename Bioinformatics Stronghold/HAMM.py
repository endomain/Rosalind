#Counting Point Mutations

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/hamm
"""

s = str(raw_input())
t = str(raw_input())

count = 0
list = []

for x in range(len(s)): 
	if s[x] != t[x]:
		count += 1

print count
	
