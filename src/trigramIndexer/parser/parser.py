class Parser(object):

    @staticmethod
    def parse(file_name):
        """
            Read in the file, and break it up into trigrams.
            return the list of trigrams.
        """
        fp = open(file_name)
        trigrams = []

        for line in fp.readlines():
            if len(line) < 3:
                trigrams.append("ANY")
            for i in range(len(line) - 2):
                trigrams.append(line[i : i + 3])

        return trigrams