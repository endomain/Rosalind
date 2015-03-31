#Strings and Lists

"""
Solution to a ROSALIND bioinformatics problem. 
Rosalind ID: endomain
URL: http://rosalind.info/problems/ini3
"""

s = str(raw_input())
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())

print s[a:b + 1] + " " + s[c:d + 1]