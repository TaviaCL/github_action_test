from unittest import TestCase
from project import Player


class Testplayer(TestCase):

    def setUp(self):
        self.p = Player("toto")

    def test_set_age(self):
        self.p.setAge(10)
        self.assertEqual(self.p.age, 10)
        self.p.setAge(15)
        self.assertEqual(self.p.age, 15)
        
 

