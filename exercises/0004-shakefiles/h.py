import glob
import os
shakespeare_path=os.path.join('tempdata', '*')
category_list = glob.glob(shakespeare_path)
print(category_list)
total_line_count = 0
nonblank_line_count = 0
file_counter = 0

for category in category_list:

	category_path = os.path.join(category, '*')
	category_filenames = glob.glob(category_path)

	for fname in category_filenames:
		file_counter += 1
		fpath = fname

		file_line_count = 0
		file_nonblank_line_count = 0
		txtfile = open(fname, 'r')
		for line in txtfile:
			total_line_count += 1
			file_line_count += 1
			if line.strip() is not "":
				nonblank_line_count += 1
				file_nonblank_line_count += 1
		txtfile.close()
		print (fname," has ", file_nonblank_line_count," out of ",
			file_line_count,"total lines. ")

print (total_line_count)
print (nonblank_line_count)

print("All together, Shakespeare's ",file_counter,
	" text files have: ",nonblank_line_count,
	" non-blank lines out of ",total_line_count,
	" total lines")




