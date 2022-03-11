// # function lexer()
// # {
// #      repeat
// #            getchar();
// #            If input char terminates a token 
// #                AND it is an accepting state then
// #                    Isolate the token/lexeme
// #                    decrement the  CP if necessary
// #           else  lookup FSM (current state, input char);
// #      until (token found) or (no more input)
     
// #     If token found then
// #           return(token)	
// # }

#include <iostream>
#include <string.h>
#include <iomanip>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

// keyword
bool isKeyword(char* str) {
    if (!strcmp(str, "if") || !strcmp(str, "else") ||
        !strcmp(str, "while") || !strcmp(str, "do")
        || !strcmp(str, "then") || !strcmp(str, "whileend") ||
        !strcmp(str, "bool") || !strcmp(str, "and") || !strcmp(str, "float")
        || !strcmp(str, "function") || !strcmp(str, "int") ||
        !strcmp(str, "char") || !strcmp(str, "true") ||
        !strcmp(str, "false") || !strcmp(str, "endif")
        || !strcmp(str, "doend") || !strcmp(str, "forend")
        || !strcmp(str, "input") || !strcmp(str, "output")
        || !strcmp(str, "or") || !strcmp(str, "not"))
        
        return true;
    else
        return false;
}