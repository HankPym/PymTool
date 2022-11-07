import json

inputstring = '''
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
'''

data = json.loads(inputstring)

for item in data["menu"]["popup"]["menuitem"]:
		print(item["onclick"])
