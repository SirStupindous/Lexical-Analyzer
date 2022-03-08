class Lexer:
    """
    The class that will perform lexical analysis, given the proper inputs.
    """
    def __init__(self, scanning, token_table, reserved_word_list):
        """
        Sets the class variables for the tables and source code.
        """
        self.scanning = scanning
        self.token_table = token_table
        self.reserved_word_list = reserved_word_list
        
    def perform_analysis(self):
        """
        The function that performs the lexical analysis.
        @return: A list of tokens representing the token stream.
        """
        self.current_token = 0
        tokens = []
        black_list = ["whitespace", "newline", "comment"]
        while self.current_token < len(self.source_code):
            token = self.__get_token()
            if token[1] in black_list:
                continue
            tokens.append(token)
        return tokens