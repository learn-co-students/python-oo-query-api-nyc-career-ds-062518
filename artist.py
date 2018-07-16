from show import Show

# Write the Artist model here:
class Artist:

    _all = []

    def __init__(self, newname):
        self._name = newname
        Artist._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, artname):
        a = [art for art in cls._all if art._name == artname]
        if len(a) == 0:
            return 'no artist'
        else:
            return a[0]

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, setname):
        self._name = setname

    def shows(self):
        return[show for show in Show.all() if show.artist == self]
