import unittest
from app.models import Subscriber

class SubModelTest(unittest.TestCase):

    def setUp(self):
        self.new_sub = Subscriber(username = 'yegon')

    def test_init(self):
        self.assertEqual(self.new_sub.username,'yegon') 