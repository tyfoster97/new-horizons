import json

data = dict(json.load(open("fish.json")))

def search(name):
    return data[name]

def get_price(name):
    return data[name]["sellPrice"]

def get_location(name):
    return data[name]["location"]

def get_loc(s):
    if (s == "o"):
        return "Ocean"
    elif (s == "po"):
        return "Pond"
    elif (s == "pr"):
        return "Pier"
    elif (s == "cl"):
        return "Clifftop"
    elif (s == "mo"):
        return "Mouth"
    elif (s == "r"):
        return "River"

def add():
    name = input("name: " )
    price = int(input("price: "))
    location = input("Location (o, po, pr, cl, mo, r")

    f = {"sellPrice": price, "location": get_loc(location)}