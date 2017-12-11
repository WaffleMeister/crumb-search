class PatternSearcher(object):

    def __init__(self):
        pass

    def search_files(self, pattern, files):
        result = []

        for file in files:
            with open(file, "r") as f:
                lines = self.search_lines(pattern, f.readlines())                
                result.extend(list(map(lambda x: self.match_string(file, x), lines)))
                
        return result

    def search_lines(self, pattern, lines):
        return [line for line in lines if pattern.search(line)]

    def match_string(self, matched_file, matched_line):
        return "{0}: {1}".format(matched_file, matched_line)










    



    
