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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def shows(self):
        return [show for show in Show.all() if self == show._artist]

    @classmethod
    def find_by_name(cls, name):
        return [artist for artist in cls.all() if artist._name == name]
