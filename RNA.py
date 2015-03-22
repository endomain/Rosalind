file1 = open(raw_input("Type your input file name exactly: "), 'r')
lines = file1.readlines()
file1.close()

lines = str(lines)

new = lines.replace('T','U')

print new
