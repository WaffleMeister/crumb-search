import unittest
import os
from src.trigramIndexer.indexer import Indexer

class TestIndexer(unittest.TestCase):

    def test_search_directory_for_indexable_files(self):
        indexer = Indexer(["java"])
        searchable_files = indexer.search_directory_for_indexable_files(os.path.abspath(os.path.join( "tst", "test_data")))
        self.assertEqual(len(searchable_files), 2)
        indexer = Indexer()
        searchable_files = indexer.search_directory_for_indexable_files(os.path.abspath(os.path.join( "tst", "test_data")))
        self.assertEqual(len(searchable_files), 6)

    def test_index_directory(self):
        indexer = Indexer()
        indexer.index_directory(os.path.abspath( os.path.join( "tst", "test_data")))
        self.assertGreater(len(indexer.index.trigramToFileSetMap), 0)