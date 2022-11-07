import json
import requests

# Using static data
in_str = """
    {"country abbreviation": "US", "places": [
        {"place name": "Belmont", "longitude": "-71.4594", "post code": "02178", 
        "latitude": "42.4464"}, 
        {"place name": "Belmont", "longitude": "-71.2044", "post code": "02478", 
        "latitude": "42.4128"}
    ],
    "country": "United States", "place name": "Belmont", 
    "state": "Massachusetts", "state abbreviation": "MA"
    }
"""
jdata = json.loads(in_str)

# Using data from web
# req = requests.get('http://api.zippopotam.us/us/ma/belmont')
# jdata = json.loads(req.text)

# print(jdata)

city = jdata['places'][0]['place name']
state = jdata['state abbreviation']
post = jdata['places'][0]['post code']
country = jdata['country']

print(city + ", " + state)
print(post)
print(country)