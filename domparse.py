import xml.dom.minidom
import requests

def main():
    url = 'http://httpbin.org/xml'
    result = requests.get(url)

    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement

    print('The root Element is {0}'.format(rootnode.nodeName))
    print('Title: {0}'.format(rootnode.getAttribute('title')))

    items = domtree.getElementsByTagName("item")
    print('There are {0} item tags'.format(items.length))

    newItem = domtree.createElement('item')

    newItem.appendChild(domtree.createTextNode('This is some text'))
    firstSlide = domtree.getElementsByTagName('slide')[0]

    firstSlide.appendChild(newItem)

    items = domtree.getElementsByTagName("item")
    print('There are {0} item tags'.format(items.length))

if __name__ == '__main__':
    main()
