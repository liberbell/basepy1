import requests

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)
    # printResults(result)

    # url = 'http://httpbin.org/get'
    url = 'http://httpbin.org/post'

    dataValues = {
        'key1': 'value1',
        'key2': 'value2'
    }
    result = requests.post(url, data=dataValues)
    printResults(result)

    url = 'http://httpbin.org/get'
    headerValues = {
        'User-Agent' : 'Joe Marini App / 1.0.0'
    }

    result = requests.get(url, headers=headerValues)
    printResults(result)

def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers: ----------------------')
    print(resData.headers)
    print('\n')

    print('Return data: ------------------')
    print(resData.text)



if __name__ == '__main__':
    main()
