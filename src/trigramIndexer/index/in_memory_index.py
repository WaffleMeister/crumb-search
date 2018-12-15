import pickle
import os

class InMemoryIndex(object):

    def __init__(self, index = {}):
        index['+'] = set()
        self.trigramToFileSetMap = index
        self.index_directory = self.__get_index_directory()
    
    def __get_index_directory(self):
        backup_path = os.path.join(os.path.expanduser('~'), '.indexDirectory')
        return os.environ.get('CSEARCHINDEX', backup_path)    

    def get_matching_files(self, trigram_list):
        matching_files = []

        for trigram in trigram_list:
            if trigram not in self.trigramToFileSetMap:
                return set() # No matching files.
            matching_files.append(self.trigramToFileSetMap[trigram])

        return set.intersection(*matching_files)

    def store_in_index(self, trigram_list, file_name):
        # All files are added to the ANY(+) set.
        self.trigramToFileSetMap['+'].add(file_name)

        for trigram in trigram_list:
            if trigram not in self.trigramToFileSetMap:
                self.trigramToFileSetMap[trigram] = set()
            self.trigramToFileSetMap[trigram].add(file_name)

    def persist(self, file_name = "index_file"):
        self.create_directory(self.index_directory)
        with open(os.path.join(self.index_directory, file_name), "wb") as f:
            pickle.dump(self.trigramToFileSetMap, f, pickle.HIGHEST_PROTOCOL)

    def create_directory(self, path):
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def load(self, file_name = "index_file"):
        with open(os.path.join(self.index_directory, file_name), "rb") as f:
            self.trigramToFileSetMap = pickle.load(f)