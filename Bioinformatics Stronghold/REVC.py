#ComplementDNA
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/revc
"""

lines = raw_input()

new = lines[::-1]

from string import maketrans
initial = "ATCG"
final = "TAGC"
trans = maketrans(initial, final)

print new.translate(trans)