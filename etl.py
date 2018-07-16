from setlist_data import data
from artist import Artist
from show import Show

def find_or_create_artist(name):
    if Artist.find_by_name(name):
        return Artist.find_by_name(name)
    else:
        return Artist(name=name)

def make_show_objects(data):
    for show in data:
        artist = find_or_create_artist(show['artist']['name'])
        date = show['eventDate']
        venue = show['venue']['name']
        location = '{}, {}'.format(show['venue']['city']['name'], show['venue']['city']['state'])
        setlist = [song['name'] for song in show['sets']['set'][0]['song']]
        Show(artist=artist,date=date,venue=venue,location=location,setlist=setlist)
