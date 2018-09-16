import json

def main():
    jsonStr = '''{
        'sandwitch' : 'Reuben',
        'toasted' : true,
        'toppings' : [
            'Thousasnd Island Dressing',
            'Sauerkraut',
            'Pickles'
        ],
        'Price' : 8.99
    }'''

    data = json.loads(jsonStr)

    print('Sandwitch: ' + data['sandwitch'])
    if (data['toasted']):
        print(('And it's toasted!'))

    for topping in data['toppings']:
        print('Toppings: ' + topping)



if __name__ == '__main__':
    main()
