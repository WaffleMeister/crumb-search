import argparse
from src.trigramIndexer.indexer import Indexer

"""
    This script asks for a directory path, indexes that directory, 
    and allows the user to type in regex queries for that indexed set.

    Future notes: Let the user specify an index, or index locaion?
"""

"""
    Options: 
    -i: index a directory
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
    parser.add_argument("-s", "--search", required=True, action="store", dest="search_term",
                        help="Regular expression to search for.")

    args = parser.parse_args()
    

    search_action(args, indexer.index, args.search_term)


def search_action(args, index, search_term):
    if (args.search_term is not None):
        print("Beginning search for: " + search_term)
    index.get_matching_files()


if __name__ == "__main__":
    main()
