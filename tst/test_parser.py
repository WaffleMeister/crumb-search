import unittest
import os
from src.trigramIndexer.parser.parser import Parser
from src.trigramIndexer.index.elastic_search_index import ElasticSearchIndex

class TestParser(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_parse(self):
        file_path = os.path.abspath("tst/test_data/file")
        trigram_list = Parser.parse(file_path)
        self.assertEqual(len(trigram_list), 61)