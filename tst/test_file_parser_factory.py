import unittest
import os
from src.trigramIndexer.parser.file_parsers.file_parser_factory import FileParserFactory

from ddt import ddt, data, unpack

@ddt
class TestParsers(unittest.TestCase):

    @data (
        (".java", "UTF8FileParser"),
        (".docx", "WordDocFileParser")
    )
    @unpack
    def test_parse(self, file_type, expected_file_parser):
        file_parser = FileParserFactory().get_parser_for_filetype(file_type)
        self.assertEqual(type(file_parser).__name__, expected_file_parser)

    # def test_parse_java(self):
    #     file_path = os.path.abspath("tst/test_data/test_directory/testJava.java")
    #     trigram_list = UTF8FileParser().parse(file_path)
    #     self.assertGreaterEqual(len(trigram_list), 0)

    # def test_parse_docx(self):
    #     file_path = os.path.abspath("tst/test_data/test_directory/testDocx.docx")
    #     trigram_list = WordDocFileParser().parse(file_path)
    #     self.assertGreaterEqual(len(trigram_list), 0)