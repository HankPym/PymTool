import requests

response = requests.get("http://www.drudgereport.com")
print(response.text)