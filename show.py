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
    def artist(self, artist):
        self._artist = artist

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        self._date = date

    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, venue):
        self._venue = venue

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        self._location = location

    @property
    def setlist(self):
        return self._setlist
    @setlist.setter
    def setlist(self, setlist):
        self._setlist = setlist
