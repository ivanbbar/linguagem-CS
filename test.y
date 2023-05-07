%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR:  %s\n", s); }
%}

%token STRING
%token IDENTIFIER 
%token INT

%token PLUS
%token MINUS
%token NOT
%token AND
%token OR
%token ASSIGMENT
%token EQUAL
%token LT
%token GT
%token DOT
%token COMMA
%token LEFTPAREN
%token RIGHTPAREN
%token COLON

%token BREAK
%token OPEN_BRACKETS
%token CLOSE_BRACKETS
%token PRINT 
%token READ 
%token WHILE 
%token IF 
%token ELSE 

%token START
%token RETURN

%token VAR
%token VAR_TYPE

%start program

%%

program : START LEFTPAREN RIGHTPAREN block
        ;

block : OPEN_BRACKETS statement CLOSE_BRACKETS
      | OPEN_BRACKETS CLOSE_BRACKETS
      ;   

statement : assigment BREAK
          | print BREAK
          | var BREAK
          | if
          | while
          | block 
          ;
        
relexpression: expression EQUAL expression
             | expression LT expression
             | expression GT expression
             | expression DOT expression
             | expression
             ;

expression: term PLUS term
          | term MINUS term
          | term OR term
          | term
          ;

term: factor
    | factor AND factor
    ;

factor: INT
      | STRING
      | IDENTIFIER
      | PLUS factor
      | MINUS factor
      | NOT factor
      | READ LEFTPAREN RIGHTPAREN
      | LEFTPAREN relexpression RIGHTPAREN
      ;

declaration: IDENTIFIER COLON VAR_TYPE
           | IDENTIFIER COMMA declaration
           ;

var: VAR declaration;

assigment: IDENTIFIER ASSIGMENT relexpression;

print: PRINT LEFTPAREN relexpression RIGHTPAREN;

if: IF LEFTPAREN relexpression RIGHTPAREN statement else;

else: ELSE statement
    | BREAK
    ;

while: WHILE LEFTPAREN relexpression RIGHTPAREN statement;

%%

int main(){
  yyparse();
  return 0;
}