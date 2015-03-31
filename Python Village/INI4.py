#Conditions and Loops

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/ini4
"""

a = int(raw_input())
b = int(raw_input())

total = 0

for x in range(a + 1,b):
	if x % 2 == 1:
		total += x

print total
