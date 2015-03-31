#Rabbits and Recurrence Relations
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/fib
"""

n = int(raw_input())
k = int(raw_input())

tn = [1,1]

for x in range(2,n):
	m = tn[x-1] + tn[x-2] * k
	tn.append(m)

print tn[-1]