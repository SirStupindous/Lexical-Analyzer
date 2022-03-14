# lexical-analyzer-project-nej
Participents -   
Ethan Stupin  ethstup@csu.fullerton.edu  
Nicholas Ayson  nick.ayson@csu.fullerton.edu  

Who did what:  
Ethan Stupin and Nicholas Ayson - Regular Expressions, DFA, All three coding files  
Nicholas Ayson - NFA, Scanning Table, Token Table, Reserved Word Table  
  
Command to RUN:  
> python3 main.py scanning.csv token_table.csv reserved_word.csv test1.txt  
> PLEASE PUT IN CUSTOM INPUT FILE

INPUT:
>int main() {  
	// This is a single line comment.  
	float _id_a_t = 10.0E+4;  
      float _id_b_t = 2.7;  
      float result = _id_a_t + _id_b_t;  
      result*=3;  
      print(result);  
>}    
  
>int main() {
    /* This is a C program. */
    printf ( "HelloWorld\n" ) ;
    return 0; 
>   }
  
OUTPUT:
>(0, ('int', 'reserved_word'))  
>(1, (' main', 'Identifier'))  
>(2, ('()', 'rightParen'))  
>(3, (' {', 'leftBrace'))  
>(4, ('//', 'multOp'))  
>(5, (' This', 'Identifier'))  
>(6, (' is', 'Identifier'))  
>(7, (' a', 'Identifier'))  
>(8, (' single', 'Identifier'))  
>(9, (' line', 'Identifier'))  
>(10, (' comment', 'Identifier'))  
>(11, ('\tfloat', 'Identifier'))  
>(12, (' _id_a_t', 'Identifier'))  
>(13, (' =', 'assignOp'))  
>(15, ('float', 'reserved_word'))  
>(16, (' _id_b_t', 'Identifier'))  
>(17, (' =', 'assignOp'))  
>(18, (' 2.7', 'floatLiteral'))  
>(19, ('float', 'reserved_word'))  
>(20, (' result', 'Identifier'))  
>(21, (' =', 'assignOp'))  
>(22, (' _id_a_t', 'Identifier'))  
>(23, (' +', 'addOp'))  
>(24, (' _id_b_t', 'Identifier'))  
>(25, ('result', 'Identifier'))  
>(26, ('*=', 'assignOp'))  
>(27, ('3;', 'Semicolon'))  
>(28, (' print', 'Identifier'))  
>(29, ('(result', 'Identifier'))  
>(30, (');', 'Semicolon'))  
>(31, ('\n}', 'rightBrace'))  

>(0, ('int', 'reserved_word'))
>(1, (' main', 'Identifier'))
>(2, ('()', 'rightParen'))
>(3, (' {', 'leftBrace'))
>(4, (' /', 'multOp'))
>(5, ('This', 'Identifier'))
>(6, (' is', 'Identifier'))
>(7, (' a', 'Identifier'))
>(9, (' program', 'Identifier'))
>(10, ('*/', 'multOp'))
>(11, (' printf', 'Identifier'))
>(12, (' (', 'leftParen'))
>(13, (' "HelloWorld\\n"', 'String'))
>(14, (' )', 'rightParen'))
>(15, (' ;', 'Semicolon'))
>(16, (' return', 'Identifier'))
>(17, (' 0', 'intLiteral'))
>(18, (' }', 'rightBrace'))
>Reached end of token stream. Ending program.