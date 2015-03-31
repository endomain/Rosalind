#RNA Splicing
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/splc
"""

f = open(raw_input("Type your input file name exactly: "), 'r')
lines = f.readlines()
f.close()

linen = []
intron = []

for x in range(0, len(lines)):
	lines[x] = lines[x].replace("\n", "")

for z in lines:
	if z[0]== ">":
		num = lines.index(z)
		linen.append(num)

s = lines[linen[0]+1:linen[1]]
s = ''.join(s)

for m in range(linen[1],linen[-1]+2):
	if m not in linen:
		intron.append(lines[m])

for y in range(0, len(intron)):		
	t = intron[y]
	l = len(t)
	for i in range(0,len(s)):
		if s[i:i+l] == t:
			s = s.replace(t,"")

ns = s.replace('T','U')

for letter in ns:
	if letter in "\n":
		ns.replace(letter,'')

table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

codons = [ns[k:k+3] for k in range(0,len(ns),3)]

AA = ""

for x in codons:
	if x in table.keys():
		if table[x] != 'STOP':
			AA += table[x]

print AA
