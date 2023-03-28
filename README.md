
# Linguagem do Jogo do C ou S

## Descrição da linguagem

Esta é uma gramática de linguagem de programação inspirada no famoso jogo de bebida C ou S. Quem falar qualquer palavra que contenha as letras C ou S, toma uma dose (ou doze). Nesta linguagem, o C e o S não são permitidos. 
Além disso, ao final de cada declaração ou bloco é necessário um gole. Abrir e virar é a sequência óbvia, nesse contexto, quando se tem um novo bloco.

A gramática define os seguintes elementos:

STATEMENT: uma instrução que pode ser executada pelo programa

FUNCTION: um bloco de código que pode ser chamado de outros lugares no programa

EXPRESSION: uma combinação de valores, variáveis e operadores

CONST_DECLARATION: um valor que não pode ser alterado durante a execução do programa

FUNCTION_CALL: uma estrutura que pode ser chamada em qualquer parte do programa

IF_STATEMENT: permite que o programa tome decisões com base em uma condição

WHILE_STATEMENT: permite que o programa execute um bloco de código repetidamente enquanto uma condição for verdadeira

STDOUT: permite que o programa imprima dados na saída

SIMPLE_EXPRESSION: uma expressão que contém um termo

TERM: uma expressão que contém um fator

FACTOR: uma expressão que pode ser um identificador, um número, uma string ou uma chamada de função

IDENTIFIER: um nome que pode ser atribuído a uma variável ou a uma função

STRING: uma sequência de caracteres delimitada por aspas duplas

CHARACTER: pode ser uma letra (maiúscula ou minúscula), um dígito, um operador matemático ou um símbolo

MATH_OPERATOR: operador matemático

COMPARISON_OPERATOR: operador de comparação

SYMBOL: símbolos especiais conhecidos, assim como símbolos específicos únicos para esta linguagem de programação: "GOLE", "ABRE" e "VIRA"

LETTER: conjunto de caracteres entre "a" e "z" ou "A" e "Z", excluido "c", "C", "s" e "S".

NUMBER: valor numérico

DIGIT: dígitos de 0 a 9


## EBNF


```javaScript

PROGRAM = { STATEMENT | FUNCTION };

STATEMENT = (EXPRESSION | STDOUT | IF_STATEMENT | WHILE_STATEMENT | CONST_DECLARATION), "GOLE";

BLOCK = "ABRE", [STATEMENT, { STATEMENT }], "VIRA";

EXPRESSION = SIMPLE_EXPRESSION, [COMPARISON_OPERATOR, SIMPLE_EXPRESSION];

SIMPLE_EXPRESSION = TERM, { ("+" | "-"), TERM };

TERM = FACTOR, { ("*" | "/"), FACTOR };

FACTOR = IDENTIFIER | "(", EXPRESSION, ")" | NUMBER | STRING | FUNCTION_CALL;

ID
ENTIFIER = LETTER, { LETTER | DIGIT | "_" };

STDOUT = "XAIDA", "(", EXPRESSION, ")";

CONST_DECLARATION = "XONSTANTE", IDENTIFIER, "=", EXPRESSION, "gole";


FUNCTION_CALL = IDENTIFIER, "(", [EXPRESSION, { ",", EXPRESSION }], ")";

FUNCTION = "FUNXAO", IDENTIFIER, ":", [FUNCTION_PARAM_LIST], BLOCK;

FUNCTION_PARAM_LIST = [FUNCTION_PARAM, { ",", FUNCTION_PARAM }];

FUNCTION_PARAM = "PARAMETRO", IDENTIFIER;



WHILE_STATEMENT = "ENQUANTO", "(", EXPRESSION, ")", BLOCK;

IF_STATEMENT = "XE", "(", EXPRESSION, ")", BLOCK, ["XENAO", BLOCK];



CHARACTER = LETTER | DIGIT | MATH_OPERATOR | SYMBOL;

MATH_OPERATOR = "+" | "-" | "/" | "*";

COMPARISON_OPERATOR = "<" | "<=" | ">" | ">=" | "==" | "!=";

SYMBOL = "." | "_" | "@" | "#" | "!" | "&" | "(" | ")" | "{" | "}" | "[" | "]" | "GOLE" | "ABRE" | "VIRA";

NUMBER = DIGIT, { DIGIT }, [".", DIGIT, {DIGIT}];

STRING = '"', { CHARACTER }, '"';

DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

LETTER = ( a | b | d | e | ... | q | r | t | u | ... | z ) | ( A | B | D | E | ... | Q | R | T | U | ... | Z );

```


## Exemplos

```javaScript
XAIDA("zandra zilvia zubmizza xervizal xervia xatixfeita o xovina xinhozinho xebaztião") gole
```

```javaScript
FUNXAO area_retangulo: PARAMETRO baze, PARAMETRO altura, ABRE
    XONXTANTE area = baze * altura GOLE
    XAIDA("A area do retangulo eh: ", area) GOLE
VIRA

area_retangulo(5, 10) GOLE
```

```javaScript
FUNXAO par_ou_impar: PARAMETRO numero, ABRE
    XE(numero % 2 == 0), ABRE
        XAIDA(numero, " eh par.") GOLE
    XENAO, ABRE
        XAIDA(numero, " eh impar.") GOLE
    VIRA VIRA
    
par_ou_impar(10) GOLE
```
