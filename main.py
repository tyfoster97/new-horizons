import api

api.load_inv()

cmd = input(":")
#a-i -> add insect
#a-f -> add fish
#s-f -> search fish
#s-i -> seach insects
#q -> quit
#w -> sell
#c -> compare
#l -> list
#r -> remove from inventory
#su-in -> edit insects
#su-fi -> edit fish

while(cmd != "q"):
    api.do_cmd(cmd)
    cmd = input(":")

api.write_inv()
