import unittest
import os
from src.trigramIndexer.parser.parser import Parser

class TestParser(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_parse(self):
        file_path = os.path.abspath("tst/test_data/test_file")

        parser = Parser()

        trigram_list = parser.parse(file_path)

        print(len(trigram_list))