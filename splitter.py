#Source Code By: Dalton Caron
#Edited by: Nicholas Ayson and Ethan Stupin
import os

class Splitter:
    def __init__(self, scanning_table_filename, token_table_filename, \
        source_filename, reserved_word_table_filename):
        self.scanning_table_filename = scanning_table_filename
        self.token_table_filename = token_table_filename
        self.source_filename = source_filename
        self.reserved_word_table_filename = reserved_word_table_filename
        self.__validate()

    def parse(self):
        return (self.__parse_lexical_table(), self.__parse_token_table(), \
            self.__parse_source_code(), self.__parse_keywords())

    def __parse_lexical_table(self):
        table_string = self.__read_file_as_string(self.scanning_table_filename)
        rows = table_string.split('\n')
        line1data = rows[0].rstrip().split(',')
        row_length = len(line1data) # asumption that all rows are same length
        char_map_string = "0"
        for i in range(1,row_length):
            char_map_string += chr(int(line1data[i]))
        lexical_table = {}
        for i in range(1, len(rows)):
            line_data = rows[i].rstrip().split(',')
            if len(line_data) != row_length:
                continue # ignore malformed row
            current_state = int(line_data[0])
            column_lookup = {}
            for j in range(1, len(line_data)):
                if len(line_data[j]) == 0 or line_data[j][0] == 13:
                    state = -1
                else:
                    state = int(line_data[j])
                column_lookup[char_map_string[j]] = state
            lexical_table[current_state] = column_lookup
        return lexical_table

    def __parse_token_table(self):
        table_string = self.__read_file_as_string(self.token_table_filename)
        rows = table_string.split('\n')
        token_table = {}
        for i in range(0, len(rows)):
            line_tuple = rows[i].split(',')
            if len(line_tuple) != 2:
                continue # skip non tuple lines
            state = int(line_tuple[0])
            token = str(line_tuple[1])
            if len(token) == 0 or token[0] == 41 :
                token = 'error'
            else:
                token = token.rstrip() # strip newline and carridge return
            token_table[state] = token
        return token_table
            

    def __parse_source_code(self):
        return self.__read_file_as_string(self.source_filename)

    def __parse_keywords(self):
        keywords_string = self.__read_file_as_string(self.reserved_word_table_filename)
        keywords_split = keywords_string.rstrip().split(',')
        keywords = [str(i) for i in keywords_split]
        return keywords

    def __validate(self):
        self.__validate_csv(self.scanning_table_filename)
        self.__validate_csv(self.token_table_filename)
        self.__validate_csv(self.reserved_word_table_filename)
        self.__file_exists(self.scanning_table_filename)
        self.__file_exists(self.token_table_filename)
        self.__file_exists(self.source_filename)
        self.__file_exists(self.reserved_word_table_filename)

    def __validate_csv(self, filename):
        if len(filename) < 5 or filename[-4:] != ".csv":
            raise ValueError("expected a .csv file, got", filename, "instead")

    def __file_exists(self, filename):
        if not os.access(filename, os.R_OK):
            raise ValueError("file",filename,"does not exist")

    def __read_file_as_string(self, filename):
        with open(filename, 'r') as file_pointer:
            return file_pointer.read()