import urllib.request
import re

print('Enter URL')
URL = input('>> ')

if re.match(r"^https?:\/\/", URL):
    print(URL)
else:
    print('Wrong URL')

# with urllib.request.urlopen(URL) as res:
#    html = res.read().decode("utf-8")
#    print(html)
