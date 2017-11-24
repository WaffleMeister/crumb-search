class ElasticSearchIndex:

    def __init__(self):
        self.index = {}
        
    def get_matching_files(self, trigram_list):
        return NotImplementedError

    def store_in_index(self, trigram_list, file_name):
        return NotImplementedError