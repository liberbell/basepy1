import json
from json import JSONDecodeError

def main():
    jsonStr = '''{
        "sandwitch" : "Reuben",
        "toasted" : true,
        "toppings" : [
            "Thousasnd Island Dressing",
            "Sauerkraut",
            "Pickles"
        ]
        "Price" : 8.99
    }'''
    try:
        data = json.loads(jsonStr)

        print('Sandwitch: ' + data['sandwitch'])
        if (data['toasted']):
            print(('And it`s toasted!'))

        for topping in data['toppings']:
            print('Topping: ' + topping)


    except JSONDecodeError as err:
        print('Whoops, JSON Decode Error: ')
        print('err.msg')
        print('Error line: {0}'.format(err.lineno), 'Error ColumNo: {0}'.format(err.colno))


if __name__ == '__main__':
    main()
