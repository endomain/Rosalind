#Transcribe DNA into RNA
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/rna
"""
file1 = open(raw_input("Type your input file name exactly: "), 'r')
lines = file1.readlines()
file1.close()

lines = str(lines)

new = lines.replace('T','U')

print new

