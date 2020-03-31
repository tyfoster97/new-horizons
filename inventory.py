import json

stuff = dict()

def add(item, data):
    stuff[item] = data

def remove(item):
    del stuff[item]

def clear():
    stuff.clear()

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

def write(name):
    with open(name, "w") as f:
        json.dump(stuff, f)

def read(name):
    with open(name) as f:
        stuff = dict(json.load(name))