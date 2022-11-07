import requests
import xml.etree.ElementTree as ET

aTitles = []
aDescs = []

r = requests.get('http://rss.cnn.com/rss/cnn_topstories.rss')

tree = ET.fromstring(r.text)


for items in tree.findall(".//channel/item"):
	for titles in items.findall("title"):
		aTitles.append(titles.text)
	for descs in items.findall("description"):
		aDescs.append(descs.text)

print(len(aTitles))
print(len(aDescs))
