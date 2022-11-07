#!/usr/bin/python
import sys

if len(sys.argv) > 1:
        strInput = sys.argv[1]
        strOutput = ""
        intLength = len(strInput)
        for count in range(intLength):
                if count > 0:
                        strOutput = strOutput + "|"
                strChar = str(strInput[count])
                print(strChar)
                if strChar == "_":
                        strChar = "32"
                elif strChar == "#":
                        strChar = "35"
                else:
                        strChar = str(ord(strChar))
                strOutput = strOutput + strChar
        strOutput = strOutput + "|13|10"
        print(strOutput)
else:
        print("Usage:\n# = numeric values to be read.\n_ = space.\n@ = Ignore.")
        print("Example: T_@_######### kg")
