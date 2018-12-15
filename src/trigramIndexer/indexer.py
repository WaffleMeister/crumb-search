import os

from src.trigramIndexer.index.elastic_search_index import ElasticSearchIndex
from src.trigramIndexer.index.in_memory_index import InMemoryIndex
from src.trigramIndexer.parser.file_parser import FileParser

class Indexer(object):
    """
        This class takes in a directory, runs a DFS on that directory, and indexes
        all the files.
    """

    def __init__(self, include_files=[], use_elastic_search=False):
        if use_elastic_search:
            self.index = ElasticSearchIndex()
        else:
            self.index = InMemoryIndex()

        self.include_files = include_files

    def search_directory_for_indexable_files(self, path):
        """
            This function is given a directory, and returns all files in that 
            directory which are of the extension we wish to index. We only 
            index files that are in the include_file list
        """
        # Get all the files in the directory
        file_list = [os.path.join(path, f) for f in os.listdir(path)]

        return_list = []

        for f in file_list:
            if os.path.isdir(f):
                return_list.extend(self.search_directory_for_indexable_files(f))
            elif self.__include_file(f):
                return_list.append(f)

        return return_list

    def index_directory(self,path):
        """
            This function takes in a file path, and indexes all applicable files
            in that path.
        """
        files = self.search_directory_for_indexable_files(path)

        for f in files:
            trigram_list = FileParser.parse(f)
            self.index.store_in_index(trigram_list, f)
        
        return self.index

    def __include_file(self, file_name):
        if len(self.include_files) == 0:
            return True
        return any(file_name.endswith(suffix) for suffix in self.include_files)