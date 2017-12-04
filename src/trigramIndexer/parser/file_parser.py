import os

class FileParser(object):

    @staticmethod
    def parse(file_name):
        """
            Read in the file, and break it up into trigrams.
            return the list of trigrams.
        """
        print("The file name is: " + file_name)

        fp = open(file_name)
        trigrams = []

        for line in fp.readlines():
            for i in range(len(line) - 2):
                trigrams.append(line[i : i + 3])

        return trigrams