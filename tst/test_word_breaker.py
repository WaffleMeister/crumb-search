import unittest
from ddt import ddt, data, unpack
from src.trigramIndexer.parser.word_breaker import WordBreaker

@ddt
class TestWordBreaker(unittest.TestCase):

    @data(
        ("batman", ["batman"]),
        ("robin", ["robin"]),
        ("rob?in", ["robin", "roin"]),
        ("bu?rg?er", ["burger", "brger", "brer", "burer"]),
        ("ca?ts", ["cats", "cts"]),
        ("bat(man|woman)", ["batman", "batwoman"]),
        ("bat(man|woman) the avenger", ["batman the avenger", "batwoman the avenger"]),
        ("bat(man|woman) the b?at", ["batman the bat", "batman the at", "batwoman the at", "batwoman the bat"]),
        ("bat(man|cant?)", ["batman", "batcant", "batcan"]),
        ("bat(man|man(child|baby))", ["batman", "batmanchild", "batmanbaby"])
    )
    @unpack
    def test_breakup_words(self, search_term, expected_parse_results):
        actual_parse_results = WordBreaker.break_apart_search_term(search_term, 0, "", [])
        # Set comparisons ignore ordering
        self.assertEqual(actual_parse_results, set(expected_parse_results))