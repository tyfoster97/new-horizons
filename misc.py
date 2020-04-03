import json

path = "/Users/charlestonpoet/git/new-horizons/resources/misc.json"
data = json.load(open(path))

# str -> dict
def search(name):
    return data[name]

# str -> int
def get_price(name):
    return data[name]["sellPrice"]

# str -> str
def get_location(name):
    return data[name]["location"]

# str -> None
def add(name):
    price = int(input("price: ")) #get price
    loc = input("location: ") #get location code

    m = {"sellPrice": price, "location": loc} #create entry

    data[name] = m # add to dict

    with open(path, "w") as f:
        json.dump(data, f)

# str -> None
def remove(name):
    data.pop(name)
    
    with open(path, "w") as f:
        json.dump(data, f)

def edit():
    cmd = "_"
    
    while cmd[0] != "q":
        cmd = input("Editing misc database\na - add\nr - remove\nq - quit\n:").split(" ", 1)
        if cmd[0] == "a":
            add(cmd[1])
        elif cmd[0] == "r":
            remove(cmd[1])
