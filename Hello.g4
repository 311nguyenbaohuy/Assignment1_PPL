/*
 * Filename : Hello.g4
 */

lexer grammar Hello;

// match any digit
INT : [0 - 9]+;

// Hexadecimal number
HEX : 0[Xx][0 - 9A - Fa - f]+;

// Match lower-case identifiers
ID : [a - z]+; 

// Skip spaces, tabs, newlines
WS : [ \t\r\n]+ ->Skip;