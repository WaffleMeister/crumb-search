import unittest
from ddt import ddt, data, unpack
from src.trigramIndexer.indexer import Indexer

import os

@ddt
class TestIndexer(unittest.TestCase):

    @data(
        ('java', 3),
        ([], 8)
    )
    @unpack
    def test_search_directory_for_indexable_files(self, file_type, expected_count):
        indexer = Indexer(file_type)
        searchable_files = indexer.search_directory_for_indexable_files(
            os.path.abspath(os.path.join("tst", "test_data")))
        self.assertEqual(len(searchable_files), expected_count)

    def test_index_directory(self):
        indexer = Indexer()
        indexer.index_directory(os.path.abspath(
            os.path.join("tst", "test_data")))
        self.assertGreater(len(indexer.index.trigramToFileSetMap), 0)
