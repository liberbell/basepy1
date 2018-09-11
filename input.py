import urllib.request
import re

print('Enter URL')
URL = input('>> ')

if re.match(r"^https?:\/\/", URL):
    print(URL)
    try:
        res = urllib.request.urlopen(URL)
        res.close()
    except urllib.request.HTTPError as reqerr:
        print('Not found: ', URL)
        print('Error Code: ' + reqerr.code)

    except urllib.request.URLError as reqerr:
        print('Not found: ', URL)
        print('Error Reason: ' + reqerr.reason)

else:
    print('Wrong URL')

# with urllib.request.urlopen(URL) as res:
#    html = res.read().decode("utf-8")
#    print(html)
