import unittest
import re
from src.trigramIndexer.searcher.pattern_searcher import PatternSearcher

class TestPatternSearcher(unittest.TestCase):

    def test_search_lines(self):
        
        pattern = re.compile("cat*")

        lines = [
            "This cat is not very nice to me.",
            "I have a new dog.",
            "I bought some blue paint yesterday.",
            "Can you come to the store?"
        ]

        result = PatternSearcher().search_lines(pattern, lines)
        self.assertEqual(len(result), 1)

    def test_search_lines_ignore_case(self):
        
        pattern = re.compile("cat*", re.IGNORECASE)

        lines = [
            "This cat is not very nice to me.",
            "I have a new dog.",
            "I bought some blue paint yesterday.",
            "Can you come to the store?"
        ]

        result = PatternSearcher().search_lines(pattern, lines)
        self.assertEqual(len(result), 2)