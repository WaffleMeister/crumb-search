import unittest
from src.trigramIndexer.parser.query_parser import QueryParser

class TestQueryParser(unittest.TestCase):
    
    def test_parse_query(self, query = "cats"):
        n_grams = QueryParser.parse_search_query(query)
        self.assertSetEqual(n_grams, {'cat','ats'})
    
    def test_parse_regex_query(self):
        self.assertSetEqual(QueryParser.parse_search_query("cat*ares"), {'are', 'res'})
        self.assertSetEqual(QueryParser.parse_search_query("cats*"), {'cat'})
        self.assertSetEqual(QueryParser.parse_search_query("cat*"), {'+'})
        self.assertSetEqual(QueryParser.parse_search_query("docu*"), {'doc'})
        self.assertSetEqual(QueryParser.parse_search_query("cat+dog"), {'cat', 'dog', 'tdo'})
        self.assertSetEqual(QueryParser.parse_search_query("cat+do*g"), {'cat'})
        self.assertSetEqual(QueryParser.parse_search_query("a+hello"), {'ahe','ell','hel','llo'})
        self.assertSetEqual(QueryParser.parse_search_query("a\+hello"), {'a+h','+he','hel', 'ell', 'llo'})
        self.assertSetEqual(QueryParser.parse_search_query("i\+\+"), {'i++'})
