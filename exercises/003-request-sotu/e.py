import requests

url = "https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address"
resp= requests.get(url)
a = resp.text
cnt= a.count ('Applause')
print (cnt)
cnt = a.lower().count ('applause')
print (cnt)
cnt=a.count ('<p>')
print (cnt)