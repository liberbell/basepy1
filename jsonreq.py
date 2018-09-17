import json
import requests

def main():
    url = 'http://httpbin.org/json'
    result = requests.get(url)

    dataobj = result.json()
    # print(json.dumps(dataobj, indent=4))

    print(list(dataobj.keys()))
    print(dataobj['slideshow']['title'])

    print('There are {0} slides'.format(len(dataobj['slideshow']['title'])))

if __name__ == '__main__':
    main()
