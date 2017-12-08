import pickle

class InMemoryIndexer(object):

    def __init__(self, index = {}):
        index['+'] = set()
        self.trigramToFileSetMap = index
        self.initialized = False
        
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

        self.initialized = True
        for trigram in trigram_list:
            if trigram not in self.trigramToFileSetMap:
                self.trigramToFileSetMap[trigram] = set()
            self.trigramToFileSetMap[trigram].add(file_name)

    def persist(self, file_name = "index_file"):
        with open(file_name, "wb") as f:
            pickle.dump(self.trigramToFileSetMap, f, pickle.HIGHEST_PROTOCOL)

    def load(self, file_name = "index_file"):
        with open(file_name, "rb") as f:
            dump = pickle.load(f)
            self.trigramToFileSetMap = dump
        self.initialized = True