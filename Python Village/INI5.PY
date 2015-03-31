#Working with Files

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/ini5
"""

file1 = open(raw_input("Type your input file name exactly: "), 'r')
lines = file1.readlines()
file1.close()

oddlines =[]

for x in lines:
	if lines.index(x) % 2 == 1:
		print x
