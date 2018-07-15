from setlist_data import data
from artist import Artist
from show import Show

def find_or_create_artist(name):
    for artist in Artist.all():
        if artist.name == name:
            return artist
    else:
        return Artist(name)

def make_show_objects(data):
    for i in range(0,len(data)):
        Show(artist = find_or_create_artist(data[i]['artist']['name']), date =  data[i]['eventDate'], venue =  data[i]['venue']['name'], location = (data[i]['venue']['city']['name'] + ', ' + data[i]['venue']['city']['state']), setlist = [item['name'] for item in data[i]['sets']['set'][0]['song']])
    return
# import pdb; pdb.set_trace()
