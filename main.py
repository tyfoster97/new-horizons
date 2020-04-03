import api

api.load_inv()

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
    if len(cmd) > 1:
        api.do_cmd(cmd[0], cmd[1])
    else:
        api.do_cmd(cmd[0])
    cmd = input(":").split(" ", 1)

if(cmd[0] == "q"):
    api.write_inv()
