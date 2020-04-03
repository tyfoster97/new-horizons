import json

path = "/Users/charlestonpoet/git/new-horizons/resources/fish.json"

data = dict(json.load(open(path)))

# str -> dict
def search(name):
    return data[name]

# str -> int
def get_price(name):
    return data[name]["sellPrice"]

# str -> str
def get_location(name):
    return data[name]["location"]

# str -> str
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

# str -> None
def add(name):
    price = int(input("price: ")) #get price
    location = input("Location (o, po, pr, cl, mo, r") #get location code

    f = {"sellPrice": price, "location": get_loc(location)} #create entry

    data[name] = f # add to dict

    with open(path, "w") as f:
        json.dump(data, f)

# str -> None
def remove(name):
    data.pop(name)
    
    with open(path, "w") as f:
        json.dump(data, f)

def edit():
    cmd = "_"
    
    while cmd != "q":
        cmd = input("Editing fish database\na - add\nr - remove\nq - quit\n:").split(" ", 1)
        if cmd[0] == "a":
            add(cmd[1])
        elif cmd[0] == "r":
            remove(cmd[1])
