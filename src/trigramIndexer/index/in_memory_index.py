import pickle

class InMemoryIndexer(object):

    def __init__(self, index = {}):
        self.index = index
        self.initialized = False
        
    def get_matching_files(self, trigram_list):
        matching_files = set()

        for trigram in trigram_list:
            if trigram not in self.index:
                return set() 
            matching_files.add(self.index[trigram])

        return set.intersection(matching_files)

    def store_in_index(self, trigram_list, file_name):
        self.initialized = True
        for trigram in trigram_list:
            if trigram not in self.index:
                self.index[trigram] = set()
            self.index[trigram].add(file_name)

    def persist(self, file_name = "index_file"):
        with open(file_name, "wb") as f:
            pickle.dump(self.index, f, pickle.HIGHEST_PROTOCOL)

    def load(self, file_name = "index_file"):
        with open(file_name, "rb") as f:
            dump = pickle.load(f)
            self.index = dump
        self.initialized = True
