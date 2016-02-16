import os
fname = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
romeofile = open(fname, 'r')
counter = 0
for x in romeofile:
	counter = counter + 1
# counter = 4000
romeofile.close()

romeofile = open(fname, 'r')
c = 0
for x in romeofile:
	c = c + 1
	if c in range (counter-5,counter+1):
		print(romeofile.readline())
romeofile.close()