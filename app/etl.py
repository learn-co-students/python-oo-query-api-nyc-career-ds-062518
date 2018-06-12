from app.setlist_data import data
from app.artist import Artist
from app.show import Show

def find_or_create_artist(name):
    if Artist.find_by_name(name):
        return Artist.find_by_name(name)
    else:
        return Artist(name=name)

def make_setlist(sets):
    setlist = []
    for set in sets:
        for song in set['song']:
            setlist.append(song['name'])
    return setlist

def make_show_objects(data):
    for show in data:
        artist = find_or_create_artist(show['artist']['name'])
        date = show['eventDate']
        venue = show['venue']['name']
        location = show['venue']['city']['name'] + ", " + show['venue']['city']['state']
        setlist = make_setlist(show['sets']['set'])
        Show(artist=artist, date=date, venue=venue, location=location, setlist=setlist)
