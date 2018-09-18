import requests
import xml.sax

class MycontentHandler(xml.sax.ContentHandler)
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0

def main():
    handler = MycountHandler()

    url = 'http://httpbin.org/xml'
    result = requests.get(url)
    print(result.text)

    print('There were {0} slide elements'.format(handler.slideCount))
    print('There were {0} item elements'.format(handler.itemCount))


if __name__ == '__main__':
    main()
