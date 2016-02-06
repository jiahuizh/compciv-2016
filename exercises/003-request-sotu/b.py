import requests

url = "http://www.sdfjfadshjdsfhjk.com"
print (url)
resp= requests.get(url)
print (resp.status_code)
print (len(resp.text))

