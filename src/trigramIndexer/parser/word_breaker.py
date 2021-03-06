class WordBreaker:

    """
        Parse apart a given phrase to its matching sub-phrases based on special
        regex characters.

        Supported chars: ?, 
                        (A | B) (OR group)

        TODO:
            Figure out if I should support nested OR operators, 
            or just throw an exeption and not support that entirely
    """
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
            """
            if current_char == '?':
                # Do something for ? characters
                WordBreaker.__handle_question_mark(
                    search_term, idx, created_term, return_list)
            if current_char == '(':
                WordBreaker.__handle_opening_bracket(
                    search_term, idx, created_term, return_list)
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
       
        start_point, pipe_idx, closing_bracked_idx = WordBreaker.__find_or_regex_indices(search_term, idx)
        
        left_choice = search_term[start_point + 1: pipe_idx]
        right_choice = search_term[pipe_idx + 1: closing_bracked_idx]

        search_term_remainder = search_term[closing_bracked_idx + 1:]

        search_term_left_choice = search_term[:start_point] + \
            left_choice + \
            search_term_remainder

        serach_term_right_choice = search_term[:start_point] + \
            right_choice + \
            search_term_remainder

        WordBreaker.break_apart_search_term(search_term_left_choice,
                                            idx,
                                            created_term,
                                            return_list)
        WordBreaker.break_apart_search_term(serach_term_right_choice,
                                            idx,
                                            created_term,
                                            return_list)

    @staticmethod
    def __find_or_regex_indices(search_term,
                                or_operand_begin):

        idx = or_operand_begin + 1

        start_point, mid_point, end_point = or_operand_begin, or_operand_begin, or_operand_begin

        nested_count = 0

        while idx < len(search_term):
            if WordBreaker.__is_special_char(search_term, idx):
                special_char = search_term[idx]

                if special_char == '(':
                    nested_count = nested_count + 1
                elif special_char == ')':
                    if nested_count == 0:
                        end_point = idx
                        break
                    nested_count = nested_count - 1
                elif special_char == '|' and nested_count == 0:
                    mid_point = idx

            idx = idx + 1

        return start_point, mid_point, end_point

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

    @staticmethod
    def __is_special_char(search_term, idx):
        if idx > 0 and search_term[idx - 1] == '\\':
            return False
        else:
            return search_term[idx] in ['?', '(', '|', ')']