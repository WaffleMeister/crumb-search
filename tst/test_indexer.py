import unittest
import os
from src.trigramIndexer.indexer import Indexer

class TestIndexer(unittest.TestCase):

    def test_index_directory(self):
        indexer = Indexer()
        indexer.index_directory("/Users/andromeda/GIT/crumb-search/tst/test_data")
        self.assertGreater(len(indexer.index.index), 0)