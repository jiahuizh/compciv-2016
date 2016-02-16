import glob
import os
tragic_path=os.path.join('tempdata', 'tragedies', '*')
tragic_filenames = glob.glob(tragic_path)

for fname in tragic_filenames:

	fpath = fname
	romeofile = open(fpath, 'r')
	counter = 0
	for x in romeofile:
		counter = counter + 1
	# counter = 4000
	romeofile.close()

	romeofile = open(fpath, 'r')
	c = 0
	for x in range(0,counter):
		c = c + 1
		if c in range (counter-4,counter+1):
			print(romeofile.readline())
		else:
			romeofile.readline()
	romeofile.close()
