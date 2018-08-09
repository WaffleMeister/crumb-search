from src.trigramIndexer.parser.query_parsing_exception import QueryParsingException

class QueryParser:

    @staticmethod
    def parse_search_query(search_query):
        """
            Given a word, parse out the trigrams
            associated with that word.

            Ex: "batman" => bat, atm, tma, man
        """
        i = 0
        return_set = set()
        n_gram = ""

        while i < len(search_query):

            char = search_query[i]

            if (QueryParser.__is_literal(char)):

                if char == '\\' and i + 1 < len(search_query):
                    next_char = search_query[i + 1]
                    if not QueryParser.__is_literal(next_char):
                        char = search_query[i + 1]
                        i += 1

                if len(n_gram) == 3:
                    return_set.add(n_gram)
                    n_gram = n_gram[1:len(n_gram)]
                n_gram += char
            else:
                if i == 0:
                    raise QueryParsingException("Can't begin regex with special char")
                elif not QueryParser.__is_literal(search_query[i - 1]) and not search_query[i - 2] == '\\':
                    invalid_nest = search_query[i - 1: i + 2]
                    raise QueryParsingException("Invalid nested repetition: {0}".format(invalid_nest))

                if char == '*':
                    n_gram = ""
                elif (char == '+'):
                    if (len(n_gram) == 3): # abc+
                        return_set.add(n_gram)
                    n_gram = n_gram[-1]
        
            i += 1
            
        if len(n_gram) == 3:
            return_set.add(n_gram)
        elif len(return_set) == 0:
            return_set.add('+')

        return return_set

    @staticmethod
    def __is_literal(char):
        return char not in ['+', '*']