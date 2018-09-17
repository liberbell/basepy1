import json

def main():
    jsonStr = '''{
        "sandwitch" : "Reuben",
        "toasted" : true,
        "toppings" : [
            "Thousasnd Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "Price" : 8.99
    }'''

    data = json.loads(jsonStr)

if __name__ == '__main__':
    main()
