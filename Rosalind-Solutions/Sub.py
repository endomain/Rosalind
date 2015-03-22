#Finding Motif in DNA
s = str(raw_input())
t = str(raw_input())

l = len(t)

for i in range(0,len(s)):
	if s[i:i+l] == t:
		print i + 1
