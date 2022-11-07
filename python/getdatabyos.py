import platform
import os
   
def getData(fileName):
    if platform.system() == "Darwin":
        pathName =  r"/Users/lfister/OneDrive/Code/data/" + fileName
    else:
        pathName = r"C:\\Users\\lesfister\\OneDrive\\Code\\data\\" + fileName

    try:
        with open(pathName) as file:
            data = file.read()
    except FileNotFoundError as err:
        return err
    return data