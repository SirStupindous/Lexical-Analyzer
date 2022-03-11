# function lexer()
# {
#      repeat
#            getchar();
#            If input char terminates a token 
#                AND it is an accepting state then
#                    Isolate the token/lexeme
#                    decrement the  CP if necessary
#           else  lookup FSM (current state, input char);
#      until (token found) or (no more input)
     
#     If token found then
#           return(token)	
#  }
class Lexer:

    def __init__(self, scanning_table, token_table, reserved_word, source_code):
        self.scanning_table = scanning_table
        self.token_table = token_table
        self.reserved_word = reserved_word
        self.source_code = source_code

    def perform_analysis(self):
        # @return: A list of tokens representing the token stream.
        self.current_token = 0
        tokens = []
        black_list = ["whitespace", "newline", "comment"]
        while self.current_token < len(self.source_code):
            token = self.__get_token()
            if token[1] in black_list:
                continue
            tokens.append(token)
        return tokens

    def __get_token(self):
        # @return: A single token.
        remembered_chars = ""
        current_state = 0
        image = ""
        remembered_state = 0
        while True:
            # gets the character in the file
            current_character = self.__get_character()
            action = self.__choose_action(current_state, current_character)
            if action == 0: # move
                if current_state in self.token_table.keys() and self.token_table[current_state] != 'error':
                    # could be in a final state
                    remembered_state = current_state
                    remembered_chars = ""
                remembered_chars += current_character
                current_state = self.scanning_table[current_state][current_character]
            elif action == 1: # recognize
                token = self.token_table[current_state]
                if not self.current_token == len(self.source_code):
                    self.current_token -= 1 # unread last read token
                break
            else: # error
                if remembered_state != 0:
                    token = self.token_table[remembered_state]
                    self.current_token -= len(remembered_chars)
                    image = image[:-len(remembered_chars)]
                    break
                return ("error at lexem number " + str(self.current_token) + \
                    ": | current lexem " + str(current_character) + " | " \
                    "| current state " + str(current_state) + " | remembered state "\
                     + str(remembered_state) , "error")
            image += current_character
        token_tuple = (image, token)
        token_tuple = self.__keyword_check(token_tuple)
        return token_tuple

    def __choose_action(self, current_state, current_character):
        if current_state in self.scanning_table.keys() and \
            current_character in self.scanning_table[current_state].keys():
            move = self.scanning_table[current_state][current_character]
            if move != -1: # valid move, so we select the move action
                return 0
        # we did not get a valid move, so we try to recognize
        if current_state in self.token_table.keys() and \
            not self.token_table[current_state] == 'error':
            return 1
        # otherwise, we are in an error state
        return 2

    def __get_character(self):
        if self.current_token < len(self.source_code):
            char = self.source_code[self.current_token]
            self.current_token += 1
            return char
        else:
            self.current_token += 1
            return 0
    
    def __keyword_check(self, token_tuple):
        if token_tuple[1] == "identifier" and token_tuple[0] in self.reserved_word:
            return (token_tuple[0], "keyword")
        return token_tuple