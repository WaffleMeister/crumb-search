class QueryParsingException(Exception):

    def __init__(self, dErrorArguments):
        Exception.__init__(self, "Invalid Regex: {0}".format(dErrorArguments))
        self.dErrorArguments = dErrorArguments