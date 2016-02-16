import os
fname = os.path.join('tempdata', 'tragedies', 'hamlet')
hamletfile = open(fname, 'r')
print(hamletfile.readline())
print(hamletfile.readline())
print(hamletfile.readline())
print(hamletfile.readline())
print(hamletfile.readline())
hamletfile.close()