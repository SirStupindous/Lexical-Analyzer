import sys
from splitter import Splitter
from lexer import Lexer

# Ensure the right amount of arguments are provided.
if len(sys.argv) != 5:
    print("python3 main.py [scanning.csv] [token_table.csv] [reserved_word.csv] [testfilehere])")
    exit(0)

# Extract file names from the program arguments.
scanning_table_filename = sys.argv[1]
token_table_filename = sys.argv[2]
reserved_word_table_filename = sys.argv[3]
source_filename = sys.argv[4]

# Construct the parser with the given files.
parser = Splitter(scanning_table_filename, token_table_filename, reserved_word_table_filename, source_filename)

try:
    # Attempt to parse provided ipnut files.
    result_quad = parser.parse()
except ValueError as ve:
    # Failed to parse an input file. End the program.
    print(ve)
    exit(0)

# Construct the lexer from the parsed file outputs from the parser.
lexer = Lexer(result_quad[0], result_quad[1], result_quad[2], result_quad[3])
# Perform the lexical analysis.
token_stream = lexer.perform_analysis()
# Prompt the user to view the tokens.
for token in enumerate(token_stream):
    print(token)
print("Reached end of token stream. Ending program.")