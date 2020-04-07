import json
import os

dirname = os.path.dirname(__file__)
path = dirname + "/resources/insects.json"
data = dict(json.load(open(path)))

# str -> dict
def search(name):
    return data[name]

def get_price(name):
    return data[name]["sellPrice"]

def get_location(name):
    return data[name]["location"]

def get_loc(s):
    if s == "f":
        return "Flying"
    elif s == "rf":
        return "Rotten Food"
    elif s == "ot":
        return "On Tree"
    elif s == "t":
        return "In Tree"
    elif s == "g":
        return "Ground"
    elif s == "ir":
        return "In Rock"
    elif s == "ts":
        return "Stump"
    elif s == "w":
        return "Water"
    elif s == "b":
        return "Beach"
    elif s == "v":
        return "Villager"
    elif s == "tr":
        return "Trash"
    elif s == "fl":
        return "Flowers"
    elif s == "u":
        return "Underground"
    elif s == "wf":
        return "White Flowers"
    elif s == "pf":
        return "Purple Flowers"
    elif s == "or":
        return "On Rock"
    else:
        return s

def add(name):
    price = int(input("price: "))
    loc = input("location (f, rf, ot, t, g, ir, ts, w, b, v, tr, fl, u, wf, pf, or): ")

    i = {"sellPrice": price, "location": get_loc(loc)}

    data[name] = i

    json.dump(data, open(path, "w"))

def remove(name):
    data.pop(name)

    json.dump(data, open(path), "w")

def edit():
    cmd = "-"

    while cmd[0] != "q":
        cmd = input("Editing insect database\na - add\nr - remove\nq - quit\n:").split(" ", 1)
        if cmd[0] == "a":
            add(cmd[1])
        elif cmd[0] == "r":
            remove(cmd[1])