# Write the Show model here:

class Show:

    _all = []

    def __init__(self, artist, date, venue, location, setlist):
        self._artist = artist
        self._date = date
        self._venue = venue
        self._location = location
        self._setlist = setlist
        Show._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self, setartist):
        self._artist = setartist
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, setdate):
        self._date = setdate
    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, setvenue):
        self._venue = setvenue
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, setlocation):
        self._location = setlocation
    @property
    def setlist(self):
        return self._setlist
    @setlist.setter
    def setlist(self, setsetlist):
        self._setlist = setsetlist
