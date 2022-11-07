from xml.etree import ElementTree

with open("C:\\Users\\Les Filling\\Desktop\\example.xml", 'rt') as xmlFile:
    tree = ElementTree.parse(xmlFile)

for node in tree.iter():
    print(node.tag, node.attrib)

node = tree.find('./with_attributes')
for name, value in sorted(node.attrib.items()):
    strName = name
    strValue = value
    print(strName + ": " + strValue)
