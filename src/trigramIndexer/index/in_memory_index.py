class InMemoryIndexer:

    def __init__(self, index = {}):
        self.index = index
        
    def get_matching_files(self, trigram_list):
        return NotImplementedError

    def store_in_index(self, trigram_list, file_name):

        if self.index[file_name] is None:
            self.index[file_name] = []
        
        self.index[file_name].extend(trigram_list)