import unittest
from src.trigramIndexer.parser.query_parser import QueryParser
from ddt import ddt, data, unpack
from src.trigramIndexer.indexer import Indexer


@ddt
class TestQueryParser(unittest.TestCase):

    @data(
        ("cat*ares", {'are', 'res'}),
        ("cats*", {'cat'}),
        ("cat*", {'+'}),
        ("docu*", {'doc'}),
        ("cat+dog", {'cat', 'dog', 'tdo'}),
        ("cat+do*g", {'cat'}),
        ("a+hello", {'ahe', 'ell', 'hel', 'llo'}),
        ("a\+hello", {'a+h', '+he', 'hel', 'ell', 'llo'}),
        ("i\+\+", {'i++'})
    )
    @unpack
    def test_parse_regex_query(self, regular_expression, expected_parse_results):
        self.assertSetEqual(QueryParser.parse_search_query(
            regular_expression), expected_parse_results)
