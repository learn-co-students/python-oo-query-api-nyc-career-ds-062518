import requests
import json


token = 'a40dcb2e-cbe0-4b88-8b79-f43e451aa71a'
headers = {'Accept': 'application/json', 'x-api-key': token}
response = requests.get('https://api.setlist.fm/rest/1.0/search/setlists?artistName=The%20Beatles&p=1&year=1965', headers=headers)

raw_data = json.loads(response.content)

# Uncomment the python debugger to play our data in the terminal
# import pdb; pdb.set_trace()

# Data is a dictionary
# check out data.keys()

# We want to clean our data to be a list of setlist dictionaries
data = raw_data['setlist']
