import json

encoder = json.JSONEncoder()
inData = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]

print(inData,"\n")

for part in encoder.iterencode(inData):
    print('PART:', part)

print(inData[0]["a"])
print(inData[0]["b"])
print(inData[0]["c"])

print("Sum of b[2] and c = ",inData[0]["b"][1] + inData[0]["c"])

