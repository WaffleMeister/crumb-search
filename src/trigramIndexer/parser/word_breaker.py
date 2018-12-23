class WordBreaker:

    @staticmethod
    def break_apart_search_term(search_term,
                                idx=0,
                                created_term="",
                                return_list=[]):
        """
            Break up a single search query to it's
            matching regular expressions. Return 
            those matching words in a list.
        """
        # Base case
        if idx == len(search_term):
            return_list.append(created_term)
            return return_list

        current_char = search_term[idx]

        # Have to look at previous character since the special char
        # can be escaped.
        if WordBreaker.__is_special_char(search_term, idx):
            """
                For '?' characters, create two versions of 
                the input word, one with, and one without the 
                preceding character. Ex:

                rob?in => roin, robin
                batm?an => batan, batman


                bat(man|woman) => batman, batwoman

                When you see a paren, skip ahead until you find a | character
                then, go on until you close that paren

                take those two substrings, and return those....
            """
            if current_char == '?':
                # Do something for ? characters
                WordBreaker.__handle_question_mark(
                    search_term, idx, created_term, return_list)
            if current_char == '(':
                pass
                # This is an opening bracket, which deliniates an OR operation
                # for a regex.

                # That's going to be different for ( | ) characters,
                # which mean some kind of split should happen.

        else:
            WordBreaker.break_apart_search_term(search_term,
                                                idx + 1,
                                                created_term + current_char,
                                                return_list)

        return set(return_list)

    @staticmethod
    def __handle_opening_bracket(search_term,
                                 idx,
                                 created_term,
                                 return_list):
        pass

    @staticmethod
    def __handle_question_mark(search_term,
                               idx,
                               created_term,
                               return_list):
        # Do not include the question mark; skip over it.
        WordBreaker.break_apart_search_term(search_term,
                                            idx + 1,
                                            created_term,
                                            return_list)
        # Skip over the question mark, and also remove the last character
        WordBreaker.break_apart_search_term(search_term,
                                            idx + 1,
                                            created_term[0:-1],
                                            return_list)

        print("Do nothing")

    @staticmethod
    def __is_special_char(search_term, idx):
        if idx > 0 and search_term[idx - 1] == '\\':
            return False
        else:
            return search_term[idx] == '?'
