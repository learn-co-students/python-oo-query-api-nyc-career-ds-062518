from setlist_data import data
from artist import Artist
from show import Show

def find_or_create_artist(name):
    artists_names = [artist._name for artist in Artist._all]
    if name in artists_names:
        return Artist.find_by_name(name)
    else:
        artist = Artist(name)
        return artist

def make_show_objects(data):
    for item in data:
        artist = find_or_create_artist(item['artist']['name'])
        date = item['eventDate']
        venue = item['venue']['name']
        location = item['venue']['city']['name'] + ", " + item['venue']['city']['state']
        setlist = [song['name'] for song in item['sets']['set'][0]['song']]
        show_obj = Show(artist, date, venue, location, setlist)
    return show_obj



# data[0]['sets']['set'][0]['song'][0]['name']
# __init__(self, artist, date, venue, location, setlist):
