#Computing GC Content

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/gc
"""

file1 = open(raw_input("Type your input file name exactly: "), 'r')
lines = file1.readlines()
file1.close()

lines = str(lines)
newlines = lines[1:len(lines)-1]
sequence = newlines.split()

ID = []
IDindex = []
Seq = []

for item in sequence:
	if item[1] == '>':
		ID.append(item[2:len(item)-4])
		IDindex.append(sequence.index(item))

for Hao in IDindex:
	if IDindex.index(Hao) < len(IDindex) - 1:
		sHao = IDindex[IDindex.index(Hao)+1]
		rHao = [''.join(sequence[Hao + 1 : sHao])]
		iSeq = ''.join(rHao)
		Seq.append(iSeq)
	elif IDindex.index(Hao) == len(IDindex) - 1:
		rHao = ''.join(sequence[Hao + 1 :])
		iSeq = ''.join(rHao)
		Seq.append(iSeq)

def GCpercent(code):
	A = float(code.count('A'))
	GC = float(code.count('C') + code.count('G'))
	T = float(code.count('T')) 
	total = A + GC + T
	return (GC * 100)/ total

Num = []

for each in Seq:
	Num.append(GCpercent(each)) 
Nseq = Num.index(max(Num))

print ID[Nseq]
print Num[Nseq]