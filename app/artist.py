from app.show import Show

# Write the Artist model here:
class Artist:
    _all = []

    def __init__(self, name):
        self._name = name
        Artist._all.append(self)

    def name():
        doc = "The name property."
        def fget(self):
            return self._name
        def fset(self, value):
            self._name = value
        def fdel(self):
            del self._name
        return locals()
    name = property(**name())

    def shows(self):
        shows = Show.all()
        return [show for show in shows if show.artist == self]

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, name):
        for artist in cls.all():
            if artist.name == name:
                return artist
