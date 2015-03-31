#Fibonacci Numbers

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/fibo
"""

listf = [0,1]
n = int(raw_input())


for x in range(1,n):
	y = listf[x-1] + listf[x]
	listf.append(y)

print listf[n]