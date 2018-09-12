import urllib.request
import urllib.parse

def main():
    url = 'http://httpbin.org/get'

    args = {
        'name': 'Joe Marini',
        'is_auther': True,
    }

    data = urllib.parse.urlencode(args)



    result = urllib.request.urlopen(url + '?' + data)

    print('Result code: {0}'.format(result.status))
    print('Returned data: ------------------')
    print(result.read().decode('utf-8'))



if __name__ == '__main__':
    main()
