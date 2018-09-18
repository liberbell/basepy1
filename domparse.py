import xml.dom.minidom
import requests

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)

    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement

    print('The root Element is {0}'.format(rootnode.nodeName))
    print('Title: {0}'.format(rootnode.getAttribute('title')))

    items = domtree,getElementsByTagName('item')
    print('There are {0} item tags'.formart(items.length))


if __name__ == '__main__':
    main()
