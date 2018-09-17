import json
import requests

def main():
    url = 'http://httpbin.org/json'
    result = requests.get(url)

    dataobj = result.json()
    print(json.dumps(dataobj, indent=4))

    print(list[dataobj.keys()])

if __name__ == '__main__':
    main()
