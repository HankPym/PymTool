import sh

print(sh.ls("-l"))

print(sh.ls(sh.glob("*.py")))

# print(sh.ifconfig("en0") 

print(sh.wc("/Users/lfister/OneDrive/Code/python/sh_play.py"))

