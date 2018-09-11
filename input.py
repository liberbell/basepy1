import urllib.request

print('Enter URL')

URL = input('>> ')
print(URL)

with urllib.request.urlopen(URL) as res:
   html = res.read().decode("utf-8")
   print(html)
