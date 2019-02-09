import time as tm

def lonzatime():
	nowtime = tm.localtime()
	lnztime = tm.strftime("%d %b %Y %H:%M",nowtime)
	return lnztime

print (lonzatime())

print (tm.daylight)