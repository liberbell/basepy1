import urllib.request

def main():
    url = 'http://httbin.org/html'

    result = urllib.request.urlopen(url)
    print('Result Code: {0}'.format(result.status))
    if (result.getcode() == 200):
        print(result.read().decode('utf-8'))


    if __name__ == '__main__':
        main()
