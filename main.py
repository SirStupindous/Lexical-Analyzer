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

import sys
import csv
from Lexer import Lexer

def main():
    
    # if len(sys.argv) != 4:
    #     print("python3 main.py [reserved_word_list.csv] [token_table.csv] [scanning.csv]")
    # exit(0)
    
    reserved_word_list_filename = sys.argv[1]
    token_table_filename = sys.argv[2]
    scanning_table_filename = sys.argv[3]


