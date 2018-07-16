from setlist_data import data
from artist import Artist
from show import Show

def find_or_create_artist(name):
    for artist in Artist.all():
        if name == artist.name:
            return artist
    else:
        return Artist(name)

# artist, date, venue, location, setlist
def make_show_objects(data):
    for i in range(0,len(data)):
        artist = find_or_create_artist(data[i]["artist"]["name"])
        date = data[i]["eventDate"]
        venue = data[i]["venue"]["name"]
        location = data[i]["venue"]["city"]["name"] + ", " + data[i]["venue"]["city"]["state"]
        # setlist = data[i]["sets"]
        setlist = []
        song_list = data[i]["sets"]["set"][0]["song"]
        for index in range(0,len(song_list)):
            setlist.append(song_list[index]["name"])
        Show(artist, date, venue, location, setlist)
    return Show.all()
