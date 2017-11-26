import argparse
from src.trigramIndexer.indexer import Indexer
from src.trigramIndexer.index.elastic_search_index import ElasticSearchIndex
from src.trigramIndexer.index.in_memory_index import InMemoryIndexer

def main():  
    include_files = ["c", "java", "py", "json", "rb"]
    include_string = ", ".join(p for p in include_files)

    parser = argparse.ArgumentParser(description=
                        "Indexer for CrumbSearch. Use this program to prepare a trigram index used by csearch.")

    parser.add_argument("-e", "--elastic", help="Use Elastic search index <REMOTE>",
                        action="store_true", default=False)
    parser.add_argument("-d", "--directory", required=True, action="store", dest="directory",
                        help="Index the specified directory.")
    parser.add_argument("-i", "--include", action="store", dest="include_files",
                        help= """File extension types that will be indexed by cIndex; others will be ignored.
                        Default: """ + include_string)

    index = None

    if (args.elastic):

    else:
        indexer = 

    args = parser.parse_args()
    indexer = Indexer(include_files, args.elastic)

    if (args.directory):
        print("Indexing directory: " + args.directory)
        indexer.index_directory(args.directory)
        indexer.index.persist()

if __name__ == "__main__":
    main()