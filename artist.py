from show import Show

# Write the Artist model here:

class Artist:
    _all = []

    def __init__(self, name):
        self._name = name
        Artist._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def shows(self):
        return [show for show in Show._all if show.artist.name == self.name]

    @classmethod
    def find_by_name(cls, name):
        #return [artist for artist in cls._all if artist.name == name]
        for artist in cls._all:
            if artist.name == name:
                return artist

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
