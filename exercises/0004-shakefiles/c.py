import shutil
shutil.unpack_archive("./tempdata/matty.shakespeare.tar.gz", extract_dir="tempdata")
print ("Unpacked tempdata/matty.shakespeare.tar.gz into: tempdata")