import api

api.load_inv()

cmd = input(":")
#i -> enter inventory
#s -> search
#q -> quit
#w -> sell
#c -> compare
#l -> list
#r -> remove
#su-in -> edit insects
#su-fi -> edit fish

while(cmd != "q"):
    api.do_cmd(cmd)
    cmd = input(":")

api.write_inv()
