import json

def main():
    pythonData = '''{
        "sandwitch" : "Reuben",
        "toasted" : true,
        "toppings" : [
            "Thousasnd Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "Price" : 8.99
    }'''

    jsonStr = json.dumps(pythonData)

    print('JSON Data: ------------------')
    print(jsonStr)

    # data = json.loads(jsonStr)
    #
    # print('Sandwitch: ' + data['sandwitch'])
    # if (data['toasted']):
    #     print(('And it`s toasted!'))
    #
    # for topping in data['toppings']:
    #     print('Topping: ' + topping)

if __name__ == '__main__':
    main()
