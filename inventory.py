import json

stuff = dict()
path = "/Users/charlestonpoet/git/new-horizons/resources/inv.json"

def add(item, data):
    stuff[item] = data
    write()

def remove(item):
    stuff.pop(item)
    write()

def clear():
    stuff.clear()
    write()

def get(item):
    return stuff[item]

def compare(data):
    less = dict()
    for item in stuff.keys():
        if stuff[item]["sellPrice"] < data["sellPrice"]:
            less[item] = stuff[item]["sellPrice"]
    return less

def all():
    return stuff

def write():
    with open(path, "w") as f:
        json.dump(stuff, f)

def load():
    with open(path) as f:
        return dict(json.load(f))

def read():
    stuff = load()

stuff = load()