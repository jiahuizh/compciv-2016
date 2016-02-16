import os
fname = os.path.join('tempdata', 'tragedies', 'hamlet')
hamletfile = open(fname, 'r')
counter = 0
for x in hamletfile:
	counter = counter + 1
hamletfile.close()

print ("tempdata/tragedies/hamlet has " + str(counter) + " lines")