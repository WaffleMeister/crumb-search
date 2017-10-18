class Parser(object):

    @staticmethod
    def parse(file_name):
        """
            Read in the file, and break it up into trigrams.

            return the list of trigrams.
        """
        file_to_read = open(file_name)
        trigrams = []

        for line in file_to_read.readline():
            if len(line) < 3:
                trigrams.append("ANY")
                break
            for i in range(len(line) - 2):
                trigrams.append(line[i : i + 3])

        return trigrams