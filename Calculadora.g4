grammar Calculadora;

// Regras principais
expr:   term (('+' | '-') term)*;        // Expressões com adição e subtração
term:   factor (('*' | '/') factor)*;    // Termos com multiplicação e divisão
factor: INT | FLOAT | ID | '(' expr ')'; // Fatores são números ou variáveis ou expressões entre parênteses

// Tokens
ID:     [a-zA-Z_][a-zA-Z_0-9]*;           // Identificadores
INT:    [0-9]+;                           // Números inteiros
FLOAT:  [0-9]* '.' [0-9]+;                // Números de ponto flutuante
WS:     [ \t\r\n]+ -> skip;               // Espaços em branco
