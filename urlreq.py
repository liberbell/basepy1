import requests

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)
    # printResults(result)

    # url = 'http://httpbin.org/post'
    url = 'http://httpbin.org/get'

    dataValues = {
        'key1': 'value1',
        'key2': 'value2'
    }
    result = requests.post(url, params=dataValues)
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
