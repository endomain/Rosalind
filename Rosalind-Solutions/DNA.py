"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/dna
"""

#Counting Nucleotides in DNA sequence
file1 = open(raw_input("Type your input file name exactly: "), 'r')
lines = file1.readlines()
file1.close()

lines = str(lines)

N_A = int(lines.count('A'))
N_C = int(lines.count('C'))
N_G = int(lines.count('G'))
N_T = int(lines.count('T'))

print N_A
print N_C
print N_G
print N_T
