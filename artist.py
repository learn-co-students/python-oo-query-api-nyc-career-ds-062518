from show import Show

# Write the Artist model here:
class Artist:
    _all = []
    def __init__(self, name):
        Artist._all.append(self)
        self._name = name

    @classmethod
    def all(cls):
        return cls._all

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def shows(self):
        return [show.artist for show in Show.all() if show.artist == self]

    @classmethod
    def find_by_name(cls,name):
        return [artist for artist in cls.all() if artist.name == name]
        
