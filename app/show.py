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

    def artist():
        doc = "The artist property."
        def fget(self):
            return self._artist
        def fset(self, value):
            self._artist = value
        def fdel(self):
            del self._artist
        return locals()
    artist = property(**artist())

    def date():
        doc = "The date property."
        def fget(self):
            return self._date
        def fset(self, value):
            self._date = value
        def fdel(self):
            del self._date
        return locals()
    date = property(**date())

    def venue():
        doc = "The venue property."
        def fget(self):
            return self._venue
        def fset(self, value):
            self._venue = value
        def fdel(self):
            del self._venue
        return locals()
    venue = property(**venue())

    def location():
        doc = "The location property."
        def fget(self):
            return self._location
        def fset(self, value):
            self._location = value
        def fdel(self):
            del self._location
        return locals()
    location = property(**location())

    def setlist():
        doc = "The setlist property."
        def fget(self):
            return self._setlist
        def fset(self, value):
            self._setlist = value
        def fdel(self):
            del self._setlist
        return locals()
    setlist = property(**setlist())
