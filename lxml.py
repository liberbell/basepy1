import requests
from lxml import etree

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)


if __name__ == '__main__':
    main()
