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


        if WordBreaker.is_special_char(search_term, idx):
            """
                For '?' characters, create two versions of 
                the input word, one with, and one without the 
                preceding character. Ex:

                rob?in => roin, robin
                batm?an => batan, batman
            """
            # Do not include the question mark itself; skip over it.
            WordBreaker.break_apart_search_term(search_term,
                                    idx + 1,
                                    created_term,
                                    return_list)
            # Skip over the question mark, and also remove the last character
            WordBreaker.break_apart_search_term(search_term,
                                    idx + 1,
                                    created_term[0:-1],
                                    return_list)
        else:
            WordBreaker.break_apart_search_term(search_term,
                                                idx + 1,
                                                created_term + current_char,
                                                return_list)

        return return_list

    @staticmethod
    def is_special_char(search_term, idx):
        if idx > 0 and search_term[idx - 1] == '\\':
            return False
        else:
            return search_term[idx] == '?'