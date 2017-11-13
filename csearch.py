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

# usage:
# crumbSearch -i DIRECTORY -s SEARCH_TERM
# crumbSearch -i DIRECTORY -s SEARCH_TERM
# crumbSearch -i DIRECTORY -e -s SEARCH_TERM
# -e points to an elastic search instance.
# use: /Users/andromeda/GIT/planout4j
# crumbSearch -i DIRECTORY -s SEARCH_TERM

parser = argparse.ArgumentParser(description=
                    "CrumbSearch; quick search for matching text over a directory corpus.")

parser.add_argument("-e", "--elastic", help="Use Elastic search index <REMOTE>",
                    action="store_true", default=False)
parser.add_argument("-i", "--index", action="store", dest="directory",
                    help="Index the specified directory.")
parser.add_argument("-s", "--search", action="store", dest="search_term",
                    help="The regex to search for.")
parser.add_argument("-d", "--depth", action="store", dest="index_depth",
                    help="Indexer directory depth (directories traversed)")

include_files = ["c", "java", "py", "json", "rb"]

args = parser.parse_args()

indexer = Indexer(include_files, args.elastic)

if (args.directory is not None):
    index_directory(indexer, args.directory)

def index_directory(indexer, file_path):
    print("Going to index directory: " + file_path)
    indexer.index_directory(file_path)
