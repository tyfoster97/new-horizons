import json

data = dict(json.load(open("fish.json")))

def search(name):
    return data[name]

def price(name):
    return data[name]["sellPrice"]

def location(name):
    return data[name]["location"]