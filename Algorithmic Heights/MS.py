#Merge Sort
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/ms
"""
f = open(raw_input("Type your input file name exactly: "), 'r')
lines = f.readlines()
f.close()

n = int(lines[0])
A = lines[1].split(" ")

for i in range(0, n):
	if "\n" in A[i]:
		A[i] = A[i].replace("\n", "")
		A[i] = int(A[i])
	else:
		A[i] = int(A[i])

A = sorted(A)

for x in range(0,n):
	print A[x],
