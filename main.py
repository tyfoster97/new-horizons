import fish
import misc
import insect as ins
import inventory as inv

inv.read()

cmd = input(":").split(" ", 1)
#ai -> add insect
#af -> add fish
#am -> add misc
#sf -> search fish
#si -> seach insects
#q -> quit
#w -> sell
#c -> compare
#l -> list
#r -> remove from inventory
#su-in -> edit insects
#su-fi -> edit fish
#su-mi -> edit misc

while(cmd[0] != "q"):
    if cmd[0] == "l":
        print(inv.all())
    elif cmd[0] == "su-in":
        ins.edit()
    elif cmd[0] == "su-fi":
        fish.edit()
    elif cmd[0] == "su-mi":
        misc.edit()
    elif cmd[0] == "ai":
        inv.add(cmd[1], ins.search(cmd[1]))
    elif cmd[0] == "af":
        inv.add(cmd[1], fish.search(cmd[1]))
    elif cmd[0] == "am":
        inv.add(cmd[1], misc.search(cmd[1]))
    elif cmd[0] == "si":
        print(ins.search(cmd[1]))
    elif cmd[0] == "sf":
        print(fish.search(cmd[1]))
    elif cmd[0] == "sm":
        print(misc.search(cmd[1]))
    elif cmd[0] == "ci":
        print(inv.compare(ins.search(cmd[1])))
    elif cmd[0] == "cf":
        print(inv.compare(fish.search(cmd[1])))
    elif cmd[0] == "cm":
        print(inv.compare(misc.search(cmd[1])))
    elif cmd[0] == "r":
        inv.remove(cmd[1])
    elif cmd[0] == "w":
        inv.clear()
    cmd = input(":").split(" ", 1)

if(cmd[0] == "q"):
    inv.write()
