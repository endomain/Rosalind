#Introduction to Protein Database
"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/dbpr
"""

from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('A9HJ86') #you can give several IDs separated by commas
record = SwissProt.read(handle)

totallist = record.cross_references
GOlist = []

for x in totallist:
	if x[0] == 'GO':
		GOlist.append(x[2])
		 
for y in GOlist:
	if y[0] == 'P':
		print y[2:]

