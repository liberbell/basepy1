import requests
from requests.auth import HTTPBasicAuth

def main():
    url = 'http://httpbin.org/basic-auth/JoeMarini/Password'

    myCreds = HTTPBasicAuth('JoeMarini', Password)
    result = requests.get(url, auth=myCreds)

    printResults(result)

def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data--------------------')
    print(resData.text)

if __name__ == '__main__':
        main()
