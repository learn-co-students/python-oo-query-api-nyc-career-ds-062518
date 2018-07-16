import unittest, sys
sys.path.insert(0, '..')
from etl import *

class TestApiObjects(unittest.TestCase):
    create_all = make_show_objects(data)

    global beatles
    beatles = Artist.all()[0]
    global first_show
    first_show = Show.all()[0]

    def test_data(self):
        self.assertEqual(len(data), 20)

    def test_artist_has_name(self):
        self.assertEqual(beatles.name, "The Beatles")

    def test_artist_has_many_shows(self):
        self.assertEqual(len(beatles.shows()), 20)

    def test_show_belongs_to_artist(self):
        self.assertEqual(first_show.artist, beatles)

    def test_show_has_a_date(self):
        self.assertEqual(first_show.date, '12-12-1965')

    def test_show_has_a_venue(self):
        self.assertEqual(first_show.venue, 'Capitol Theatre')

    def test_show_has_a_properly_formatted_location(self):
        self.assertEqual(first_show.location, 'Cardiff, Wales')

    def test_show_has_a_correct_setlist(self):
        setlist = ['I Feel Fine', "She's a Woman", 'If I Needed Someone', 'Act Naturally', 'Nowhere Man', "Baby's in Black", 'Help!', 'We Can Work It Out', 'Yesterday', 'Day Tripper', "I'm Down"]
        self.assertEqual(first_show.setlist, setlist)
