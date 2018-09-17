import json
from json import JSONDecodeError

def main():
    jsonStr = '''{
        "sandwitch" : "Reuben",
        "toasted" : true,
        "toppings : [
            "Thousasnd Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "Price" : 8.99
    }'''
    try:
        data = json.loads(jsonStr)

    except JSONDecodeError as err:
        print('Whoops, JSON Decode Error: ')
        print('err.msg')

    print('Sandwitch: ' + data['sandwitch'])
    if (data['toasted']):
        print(('And it`s toasted!'))

    for topping in data['toppings']:
        print('Topping: ' + topping)


if __name__ == '__main__':
    main()
