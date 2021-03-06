import argparse
from src.trigramIndexer.indexer import Indexer
from src.trigramIndexer.index.elastic_search_index import ElasticSearchIndex
from src.trigramIndexer.index.in_memory_index import InMemoryIndex

def main():  
    include_files = ["c", "java", "py", "json", "rb", "txt", "go", "cs"]
    include_string = ", ".join(p for p in include_files)

    parser = argparse.ArgumentParser(description= 
                        "Indexer for CrumbSearch. Use this program to prepare a trigram index used by csearch.")

    parser.add_argument("-e", "--elastic", help="Use Elastic search index <REMOTE><INCOMPLETE>",
                        action="store_true", default=False)
    parser.add_argument("-d", "--directories", action="store", dest="directories",
                        help="List of directories (comma sparated) to index.", required=True)
    parser.add_argument("-i", "--include", action="store", dest="include_files",
                        help= """
                                A space separated list of extension types that will 
                                be indexed by cIndex; others will be ignored. Files 
                                should be UTF-8 encoded. Default: 
                              """ + include_string)

    args = parser.parse_args()

    if (args.include_files):
        include_files = args.include_files.split(',')
        print("Indexing files of type: " + ', '.join(include_files))

    indexer = Indexer(include_files, args.elastic)

    print("Indexing directory: " + args.directories)

    for directory in args.directories.split(','):
        indexer.index_directory(directory)

    indexer.index.persist()

if __name__ == "__main__":
    main()
