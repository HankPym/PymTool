import os, sys

issue = input("Enter the issue: ")
if (issue != ""):
    mainpath = "C:\\Users\\Local Fister\\OneDrive\\Documents\\Fantastic Four\\"
    with open('fffiles.txt','r') as inf:
        mydict = eval(inf.read())
    inf.close()
    
    mypath = mainpath + mydict.get(issue)
    os.startfile(mypath)
else:
    print("You need to give me a name.")
