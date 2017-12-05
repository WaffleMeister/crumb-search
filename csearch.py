import argparse
from src.trigramIndexer.index.in_memory_index import InMemoryIndexer
from src.trigramIndexer.parser.query_parser import QueryParser

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

    parser.add_argument("-e", "--elastic", help="Use Elastic search index <REMOTE>",
                        action="store_true", default=False)
    parser.add_argument("-f", "--index_file", help="""The index file to use. If not specified, a default file
                                 will be used instead. Please note that the default file 
                                 is just an expected location on disk; there is no default 
                                 index and you are expected to create one with cindex.""",
                        action="store_true", dest="index_file", default="index_file")
    parser.add_argument("-s", "--search", required=True, action="store", dest="search_term",
                        help="Regular expression to search for.")

    args = parser.parse_args()

    index = None
    try:
        index = InMemoryIndexer()
        index.load(args.index_file)
        print("index loaded successfully!")
    except FileNotFoundError as f:
        quit("No index file found on disk. Run cindex to create an index.")

    n_grams = QueryParser.parse_search_query(args.search_term)

    joined_grams = " ".join(n_grams)
    print("Your N Grams are: " + joined_grams)

if __name__ == "__main__":
    main()
