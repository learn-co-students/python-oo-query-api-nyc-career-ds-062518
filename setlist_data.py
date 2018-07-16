import requests
import json
from config import *

# Make your API request here
headers = {'Accept': 'application/json', 'x-api-key': token}
response = requests.get('https://api.setlist.fm/rest/1.0/search/setlists?artistName=The%20Beatles&p=1&year=1965', headers=headers)
raw_data = json.loads(response.content)

# Uncomment the python debugger to play our data in the terminal
# import pdb; pdb.set_trace()
#
# for i in raw_data.keys():
#     print(i)
#     value = raw_data[i]
#     print(type(value))
#
# type
# <class 'str'>
# itemsPerPage
# <class 'int'>
# page
# <class 'int'>
# total
# <class 'int'>
# setlist
# <class 'list'>

# Data is a dictionary
# check out data.keys()

# We want to clean our data to be a list of setlist dictionaries
data = [setlist for setlist in raw_data['setlist']]
