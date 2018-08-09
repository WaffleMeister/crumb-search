import argparse
import re
from src.trigramIndexer.index.in_memory_index import InMemoryIndex
from src.trigramIndexer.parser.query_parser import QueryParser
from src.trigramIndexer.searcher.pattern_searcher import PatternSearcher

"""
    This script asks for a directory path, indexes that directory, 
    and allows the user to type in regex queries for that indexed set.

    Future notes: Let the user specify an index, or index locaion?
"""

"""
    Options: 
    -q: string query to use
    -e: use Elastic search instead of localized search
"""

def main():

    parser = argparse.ArgumentParser(description="""
                            CrumbSearch; quick search for matching text over a trigram index. If there is no
                            existing trigram index on disk to search with, you can make one by running the cindex
                            program.
                        """)

    parser.add_argument("-b", "--bruteforce", help="Brute force search",
                        action="store_true", default=False)
    parser.add_argument("-i", "--ignorecase", help="Case insensitive search",
                        action="store_true", default=False)
    parser.add_argument("-v", "--verbose", help="Enable verbose logging",
                        action="store_true", default=False)
    parser.add_argument("-e", "--elastic", help="Use Elastic search index <REMOTE>",
                        action="store_true", default=False)
    parser.add_argument("-f", "--index_file", help="""The index file to use. If not specified, a default file
                                 will be used instead. Please note that the default file 
                                 is just an expected location on disk; there is no default 
                                 index and you are expected to create one with cindex.""",
                        action="store", dest="index_file", default="index_file")
    parser.add_argument("-s", "--search", required=True, action="store", dest="search_term",
                        help="Regular expression to search for.")

    args = parser.parse_args()

    index = None
    try:
        index = InMemoryIndex()
        index.load(args.index_file)
    except OSError:
        quit("No index file found on disk. Run cindex to create an index.")

    if args.bruteforce:
        n_grams = {'+'}
    else:
        n_grams = QueryParser.parse_search_query(args.search_term.lower())

    matching_files = index.get_matching_files(n_grams)

    if (args.verbose):
        print("Index loaded successfully!")
        print("Your N Grams are: " + list_to_string(n_grams))
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
