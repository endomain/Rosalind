#Merge two sorted arrays

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/mer
"""

f = open(raw_input("Type your input file name exactly: "), 'r')
lines = f.readlines()
f.close()

n = int(lines[0])
m = int(lines[2])
A = lines[1].split(" ")
B = lines[3].split(" ")

C = A + B

for i in range(0, n + m):
	if "\n" in C[i]:
		C[i] = C[i].replace("\n", "")
		C[i] = int(C[i])
	else:
		C[i] = int(C[i])

C = sorted(C)

for x in range(0,n+m):
	print C[x],