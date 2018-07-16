from setlist_data import data
from artist import Artist
from show import Show

def find_or_create_artist(name):
    if Artist.find_by_name(name) == 'no artist':
        return Artist(name)
    else:
        return Artist.find_by_name(name)

def make_show_objects(data):
    for set in data:
        artiste = find_or_create_artist(set['artist']['name'])
        date = set['eventDate']
        venue = set['venue']['name']
        location = set['venue']['city']['name'] + ", " + set['venue']['city']['state']
        setlist = []
        for song in set['sets']['set'][0]['song']:
            setlist.append(song['name'])
        Show(artiste, date, venue, location, setlist)
