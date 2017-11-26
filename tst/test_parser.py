import unittest
import os
from src.trigramIndexer.parser.parser import Parser

class TestParser(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_parse(self):
        file_path = os.path.abspath("tst/test_data/file")
        trigram_list = Parser.parse_file(file_path)
        self.assertEqual(len(trigram_list), 61)

    def test_parse_java(self):
        file_path = os.path.abspath("tst/test_data/test_directory/testJava.java")
        trigram_list = Parser.parse_file(file_path)
        self.assertGreaterEqual(len(trigram_list), 0)