from xml.dom import minidom

myValues = ""
myCounter = mySum = 0

xmldoc = minidom.parse('inXML.xml')
itemlist = xmldoc.getElementsByTagName('item') 
listSize =  len(itemlist)

for s in itemlist :
    print(s.attributes['name'].value, ": ",s.attributes['value'].value)

for s in itemlist :
    myValues = myValues + s.attributes['value'].value
    myCounter += 1
    if (myCounter < listSize):
        myValues  = myValues + " + "

for s in itemlist :
    mySum =  mySum + int(s.attributes['value'].value)

print(myValues,"=",mySum)
