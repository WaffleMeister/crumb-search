import os

class UTF8FileParser(object):

    def parse(self, file_name):
        """
            Read in the file, and break it up into trigrams.
            return the list of trigrams.
        """
        try:
            fp = open(file_name, encoding='utf-8')
            trigrams = []

            for line in fp.readlines():
                for i in range(len(line) - 2):
                    trigrams.append(line[i : i + 3].lower())

            fp.close()
            return trigrams
        except UnicodeDecodeError:
            print("Skipping file: ", file_name)
            return []