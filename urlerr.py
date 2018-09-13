import urllib.request

def main():
    url = 'http://httpbin.org/html'
    # url = 'http://httpbin.org/status/404'
    # url = 'http://no-such-server.org'

    result = urllib.request.urlopen(url)
    print('Result Code: {0}'.format(result.status))
    if (result.getcode() == 200):
        print(result.read().decode('utf-8'))


if __name__ == '__main__':
        main()
