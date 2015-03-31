#Insertion Sort

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/ins
"""

f = open(raw_input("Type your input file name exactly: "), 'r')
lines = f.readlines()
f.close()

n = int(lines[0])
A = lines[1].split(" ")

for i in range(0,len(A)):
	if "\n" in A[i]:
		A[i] = A[i].replace("\n", "")
		A[i] = int(A[i])
	else: 
		A[i] = int(A[i])

print A

num = 0

x = 1
while x < n and x >= 1:
	k = A[x]
	l = A[x-1]
	if k < l:
		A[x-1] = k
		A[x] = l
		num += 1
		if x > 1:
			x -= 1
		else:
			x += 1
	else:
		x += 1

print num
