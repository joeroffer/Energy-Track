import requests
#library to send web requests
"""
web request is a message sent by a client, like a web browser, to a server, asking for something like data
"""

import json

API_KEY = 'xF5K4l2g94YHgPStpO9rhhBsjaICI2NlSLldig0C'


url = f"https://api.eia.gov/v2/natural-gas/pri/sum/data/?api_key={API_KEY}"

params = 3

response = requests.get(url)
data = response.json()
#when the data is pulled with request.get, it returns the data in a massive string
#,json() is a method that converts that long text into an object using JSON rules
# BEFORE: '{"data":[{"date":"2024-01","value":3.21}]}'
# AFTER:
# {
#   "data": [
#     {
#       "date": "2024-01",
#       "value": 3.21
#     }
#   ]
# }

#Now we can access values like a regular dictionary
"""
the response object has a few attributes
status code
meta data about the response


remember, an object is formed from a class:
ex:
car.drive(), where drive() is the method
the method is a function defined inside the class
"""
print('data successfully pulled')

#with always runs cleanup after the block completes
#with may include things like closing a file
with open("data/raw.json", "w") as f:
    json.dump(data, f, indent=2)