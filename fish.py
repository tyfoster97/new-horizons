import json

data = dict(json.load(open("fish.json")))

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
def add():
    name = input("name: " ) #get name
    price = int(input("price: ")) #get price
    location = input("Location (o, po, pr, cl, mo, r") #get location code

    f = {"sellPrice": price, "location": get_loc(location)} #create entry

    data[name] = f # add to dict

    with open("fish.json", "w") as f:
        json.dump(data, f)

# str -> None
def remove():
    name = input("name: ") #get name

    data.pop(name)
    
    with open("fish.json", "w") as f:
        json.dump(data, f)

def edit():
    cmd = "_"
    
    while cmd != "q":
        cmd = input("Editing fish database\na - add\nr - remove\nq - quit\n:")
        if cmd == "a":
            add()
        elif cmd == "r":
            remove()
