import argparse
import re
from src.trigramIndexer.index.in_memory_index import InMemoryIndex
from src.trigramIndexer.parser.query_parser import QueryParser
from src.trigramIndexer.parser.word_breaker import WordBreaker
from src.trigramIndexer.searcher.pattern_searcher import PatternSearcher

"""
    This script asks for a directory path, indexes that directory, 
    and allows the user to type in regex queries for that indexed set.
"""

def main():

    parser = argparse.ArgumentParser(description=
                        """
                            CrumbSearch; quick search for matching text over a trigram index. If there is no
                            existing trigram index on disk to search with, you can make one by running the cindex
                            program.

                            The index file is stored/loaded from one of two places:
                                A) The directory pointed to by the CSEARCHINDEX environment variable.
                                B) Failing that, the index is stored in $HOME/.indexDirectory
                            
                            In both cases, the index file itself is just named indexFile.
                        """)

    parser.add_argument("-b", "--bruteforce", help="Brute force search",
                        action="store_true", default=False)
    parser.add_argument("-i", "--ignorecase", help="Case insensitive search",
                        action="store_true", default=False)
    parser.add_argument("-v", "--verbose", help="Enable verbose logging",
                        action="store_true", default=False)
    parser.add_argument("-s", "--search", required=True, action="store", dest="search_term",
                        help="Regular expression to search for.")

    args = parser.parse_args()

    index = None
    try:
        index = InMemoryIndex()
        index.load()
        if (args.verbose): 
            print("Index loaded successfully!") 
    except OSError:
        quit("No index file found on disk. Run cindex to create an index.")

    n_gram_list = []
    
    if args.bruteforce:
        n_gram_list = [{'+'}]
    else:
        search_terms = WordBreaker.break_apart_search_term(args.search_term.lower())

    if (args.verbose):
        print("Your N Grams are: " + list_to_string(n_gram_list))
    
    for term in search_terms:
        n_gram_list.append(QueryParser.parse_search_query(term))

    matching_files = set()

    for n_grams in n_gram_list:
        for match in index.get_matching_files(n_grams):
            matching_files.add(match)

    if (args.verbose):
        print ("Found {0} candidate files:\n{1}".format( len(matching_files), list_to_string(matching_files, "\n")))

    pattern = re.compile(args.search_term, re.IGNORECASE) if args.ignorecase else re.compile(args.search_term)

    searcher = PatternSearcher()

    matches = searcher.search_files(pattern, matching_files)

    print("Found {0} matches.".format(len(matches)))

    for match in matches:
        print(match)

def list_to_string(collection, delimeter = " "):
    return delimeter.join(collection)

if __name__ == "__main__":
    main()
