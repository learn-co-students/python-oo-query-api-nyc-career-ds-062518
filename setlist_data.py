import requests
import json
from config import *

# Make your API request here
headers = {'Accept': 'application/json', 'x-api-key': token}

response = requests.get('https://api.setlist.fm/rest/1.0/search/setlists?artistName=%22The%20Beatles%22&p=1&year=1965',
headers=headers)

raw_data = json.loads(response.content)



# Uncomment the python debugger to play our data in the terminal

# Data is a dictionary
# check out data.keys()

# We want to clean our data to be a list of setlist dictionaries
data = raw_data['setlist']
# import pdb; pdb.set_trace()
