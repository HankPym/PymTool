import bs4 as BeautifulSoup
import bs4 as CData

data = open("/Users/lfister/OneDrive/Code/data/html_doc")
soup = BeautifulSoup.data
print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id="link3"))

for link in soup.find_all('a'):
    print(link.get('href'))
  
print(soup.get_text())

print("-----------------------------")

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print(type(tag))

tag.name = "blockquote"
print(tag)

print(tag.name)
print(tag['class'])
print(tag.attrs)

tag['class'] = 'verybold'
tag['id'] = 1
print(tag)

del tag['class']
del tag['id']
print(tag)

print(tag.string)




unicode_string = unicode(tag.string)
print(unicode_string)
print(type(unicode_string))

tag.string.replace_with("No longer bold")
print(tag)

print("-----------------------------")

css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print(css_soup.p['class'])

css_soup = BeautifulSoup('<p class="body"></p>')
print(css_soup.p['class'])

id_soup = BeautifulSoup('<p id="my id"></p>')
print(id_soup.p['id'])

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']

print("-----------------------------")

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
print(comment)
print(type(comment))

print("-----------------------------")

cdata = CData("A CDATA block")
comment.replace_with(cdata)
print(soup.b.prettify())

print("-----------------------------")

soup = BeautifulSoup(open("/Users/lesfister/OneDrive/Code/data/html_doc"))
soup.head
soup.title
soup.body.b
soup.a
soup.find_all('a')

head_tag = soup.head
head_tag

head_tag.contents

title_tag = head_tag.contents[0]
title_tag
title_tag.contents
len(soup.contents)
soup.contents[0].name

for child in title_tag.children:
	print(child)

for child in head_tag.descendants:
	print(child)
print(len(list(soup.descendants)))

title_tag = soup.title
print(title_tag)
print(title_tag.parent)