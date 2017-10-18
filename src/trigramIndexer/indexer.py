import os
from trigramIndexer.index.elastic_search_index import ElasticSearchIndex
from trigramIndexer.index.in_memory_index import InMemoryIndexer
from trigramIndexer.parser.parser import Parser

class Indexer(object):
    """
        This class takes in a directory, runs a DFS on that directory, and indexes
        all the files.
    """

    def __init__(self, ignore_files = [], use_elastic_search=False):
        if use_elastic_search:
            self.index = ElasticSearchIndex()
        else:
            self.index = InMemoryIndexer()
        
        self.ignore_files = ignore_files


    def index_directory(self, file_path):
        # filter out all ignorable files in this directory.
        file_names = [file_name for file_name in os.listdir(file_path) if not self.ignore_file(file_name)]

        for file_name in file_names:
            if os.path.isdir(file_name):
                self.index_directory(file_name)
            else:
                trigram_list = Parser.parse(file_name)
                self.index.store_in_index(trigram_list, file_name)
        
    def ignore_file(self, file_name):
        return any(file_name.endswith(suffix) for suffix in self.ignore_files)