class QueryParser:

    @staticmethod
    def parse_search_query(search_query):
        ''' This class takes in a single search query, and parses it out to 
            a set of trigrams the rest of the program can support.

            Supported regular expressions:

            *
            +
            ?


            duc*ccccccc => "ccc"
            duc+catrat => "atr" "cat" "cca" "duc" "rat" "tra"
        '''
        # Handle invalid regular expressions.
        if (search_query is None):
            return IOError("Search query is blank.")
        if (search_query[0] in ["*", "+", "?"]):
            return IOError("Invalid REGEX passed in.")

        # Case where search query is too small, search all files.
        if len(search_query) <= 2:
            return {'+'}

        i = 0

        return_set = set()

        while i < len(search_query) - 2:
            n_gram = search_query[i : i + 3]

            if ("*" in n_gram):
                return_set.add('+')
            elif (i + 3  < len(search_query) and search_query[i + 3] == '*'):
                return_set.add('+')
            else:
                return_set.add(n_gram) 

            i += 1           

        return return_set