import fish
import inventory as inv
import insect as ins

def do_cmd(cmd):
    if cmd == "a-i":
        s = input("name: ")
        inv.add(item=s, data=ins.search(s))
    elif cmd == "a-f":
        s = input("name: ")
        inv.add(item=s, data=fish.search(s))
    elif cmd == "s-i":
        ins.search(name=input("name: "))
    elif cmd == "s-f":
        fish.search(name=input("name: "))
    elif cmd == "su-in":
        ins.edit()
    elif cmd == "su-fi":
        fish.edit()
    elif cmd == "r":
        inv.remove(name=input("name: "))
    elif cmd == "w":
        inv.clear()
    elif cmd == "c-i":
        i = ins.search(name=input("name: "))
        inv.compare(i)
    elif cmd == "c-f":
        f = fish.search(name=input("name: "))
        inv.compare(f)
        

def write_inv():
    inv.write("inv.json")

def load_inv():
    inv.read("inv.json")