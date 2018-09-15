import requests
from requests import HTTPError

def main():
    try:
        url = 'http://httpbin.org/status/404'
        result = requests.get(url)
        result.raise_for_status()
        printResults(result)

    except HTTPError as err:
        print('Error: {0}'.format(err))

def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data: ------------')
    print(resData.text)


    # try:
    #     result = urllib.request.urlopen(url)
    #     print('Result Code: {0}'.format(result.status))
    #     if (result.getcode() == HTTPStatus.OK):
    #         print(result.read().decode('utf-8'))
    #
    # except HTTPError as err:
    #     print('Error: {0}'.format(err.code))
    #
    # except URLError as err:
    #     print ('Yeah that server is bunk. {0}'.format(err.reason))


if __name__ == '__main__':
        main()
