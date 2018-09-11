import urllib.request

def main():
    url = 'http://httpbin.org/xml'

    result = urllib.request.urlopen(url)
    print('Result code: {0}'.format.(result.status))
