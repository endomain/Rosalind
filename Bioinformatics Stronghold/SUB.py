#Finding Motif in DNA
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/sub.py
"""
s = str(raw_input())
t = str(raw_input())

l = len(t)

for i in range(0,len(s)):
	if s[i:i+l] == t:
		print i + 1