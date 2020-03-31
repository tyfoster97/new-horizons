import fish
import inventory as inv

def do_cmd(cmd):
    if cmd == "i":
        name = input("name: ")
        inv.add(name, fish.search(name))
    elif cmd == "s":
        print(fish.search(name=input("name: ")))
    elif cmd == "w":
        inv.clear()
    elif cmd == "c":
        print(inv.compare(data=fish.search(name=input("name: "))))
    elif cmd == "l":
        print(inv.all())
    elif cmd == "r":
        inv.remove(item=input("name: "))

def write_inv():
    inv.write("inv.json")

def load_inv():
    inv.read("inv.json")