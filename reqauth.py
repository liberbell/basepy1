import requests

def main():
    url = 'http://httpbin.org/basic-auth/JoeMarini/Password'

    printResults(result)

def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Returned data--------------------')
    print(resData.text)

if __name__ == '__main__':
        main()
