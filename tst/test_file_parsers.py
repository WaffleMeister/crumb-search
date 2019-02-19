import unittest
import os

from src.trigramIndexer.parser.file_parsers.utf8_file_parser import UTF8FileParser
from src.trigramIndexer.parser.file_parsers.word_doc_file_parser import WordDocFileParser

class FileParserTest(unittest.TestCase):

    def test_parse_java(self):
        file_path = os.path.abspath("tst/test_data/test_directory/testJava.java")
        trigram_list = UTF8FileParser().parse(file_path)
        self.assertEqual(len(trigram_list), 1575)

    def test_parse_docx(self):
        file_path = os.path.abspath("tst/test_data/test_directory/testDocx.docx")
        trigram_list = WordDocFileParser().parse(file_path)
        self.assertEqual(len(trigram_list), 734)