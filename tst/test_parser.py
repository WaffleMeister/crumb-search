import unittest
from src.trigramIndexer.parser.parser import Parser

class TestParser(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

