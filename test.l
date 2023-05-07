%{
#include <stdio.h>
#include <string.h>
#include "y.tab.h"
%}

%%

[\t\n]

"+"                                             return PLUS;
"-"                                             return MINUS;
"!"                                             return NOT;
"e"                                             return AND;
"ou"                                            return OR;
"="                                             return ASSIGMENT;
"=="                                            return EQUAL;
"<"                                             return LT;
">"                                             return GT;
"."                                             return DOT;
","                                             return COMMA;
"("                                             return LEFTPAREN;
")"                                             return RIGHTPAREN;
":"                                             return COLON;

"gole"                                          return BREAK;
"abre"                                          return OPEN_BRACKETS;
"vira"                                          return CLOSE_BRACKETS;
"xaida"                                         return PRINT;
"kaptar"                                        return READ;
"enquanto"                                      return WHILE;
"xe"                                            return IF;
"xenao"                                         return ELSE;

"komprakatuaba"                                 return START;
"entregue"                                      return RETURN;

"variavel"                                      return VAR;    
"inteiro"                                       return VAR_TYPE;
"vokabulo"                                      return VAR_TYPE;

[a-bd-rt-zA-BD-RT-Z0-9]+                        return STRING;
[a-bd-rt-zA-BD-RT-Z_][_a-bd-rt-zA-BD-RT-Z0-9]+  return IDENTIFIER;
[0-9]+                                          return INT;


.                                               printf("token invalido\n"); 

%%

int yywrap(void) {
    return 1;
}