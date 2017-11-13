import os

from src.trigramIndexer.index.elastic_search_index import ElasticSearchIndex
from src.trigramIndexer.index.in_memory_index import InMemoryIndexer
from src.trigramIndexer.parser.parser import Parser

class Indexer(object):
    """
        This class takes in a directory, runs a DFS on that directory, and indexes
        all the files.
    """

    def __init__(self, include_files=[], use_elastic_search=False):
        if use_elastic_search:
            self.index = ElasticSearchIndex()
        else:
            self.index = InMemoryIndexer()

        self.include_files = include_files

    def index_directory(self, file_path):
        """
            This function takes in a file path, and indexes all applicable files
            in that path.
        """
        file_names = [file_name for file_name in os.listdir(file_path) if self.__include_file(file_name)]

        # Perform a DFS on a given directory. Iterate over all the files,
        # recurse on directories.
        for file_name in file_names:
            if os.path.isdir(file_name):
                self.index_directory(file_name)
            else:
                trigram_list = Parser.parse(file_name)
                self.index.store_in_index(trigram_list, file_name)
        
        return self.index

    def __include_file(self, file_name):
        if len(self.include_files) == 0:
            return True
        return any(file_name.endswith(suffix) for suffix in self.include_files)