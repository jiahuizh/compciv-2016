import requests

print ("Downloading: http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz")
resp = requests.get('http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz')
thedata = resp.content
type(thedata)

print ("Writing file: tempdata/matty.shakespeare.tar.gz")
zfile = open("./tempdata/matty.shakespeare.tar.gz", "wb")
zfile.write (thedata)
zfile.close()