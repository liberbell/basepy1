import urllib.request
import urllib.parse

def main():
    url = 'http://httpbin.org/get'

    args = {
        'name': 'Joe Marini',
        'is_auther': True,
    }


    result = urllib.request.urlopen(url)

    print('Result code: {0}'.format(result.status))
    print('Returned data: ------------------')



if __name__ == '__main__':
    main()
