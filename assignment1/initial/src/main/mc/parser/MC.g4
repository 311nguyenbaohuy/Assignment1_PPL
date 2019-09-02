grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}

program  : mctype 'main' LB RB LP body? RP EOF ;

mctype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;


// ID: [a-zA-Z]+ ;
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LSB: '[';

RSB: ']';

LP: '{';

RP: '}';

SEMI: ';' ;

COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;

// Comment

LINE_COMMENT: '//'~[\n\r]* -> skip;
BLOCK_COMMENT: '/*'(.)*'*/'-> skip;
        
// Token set

INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

BOOLEANTYPE: 'boolean';

FLOATTYPE: 'float';

STRINGTYPE: 'string';

RETURN: 'return';

BREAK: 'break';

CONTINUE: 'continue';

IF: 'if';

ELSE: 'else';

FOR: 'for';

WHILE: 'while';

DO: 'do';

TRUE: 'true';

FALSE: 'false';

// Operator

ADD_OP: '+';

MUL_OP: '*';

LOGIC_NOT_OP: '!';

LOGIC_OR_OP: '||';

NOT_EQUAL_OP: '!=';

LESS_OP: '<';

LESS_EQUAL_OP: '<=';

ASSIGN_OP: '=';

SUB_OP: '-';

MODULUS_OP: '%';

DIV_OP: '/';

LOGIC_AND: '&&';

EQUAL_OP: '==';

GREATER_OP: '>';

GREATER_EQUAL_OP: '>=';

// Literals

fragment Digit: [0-9];
INT_LIT: Digit+;


fragment Point: '.';
fragment Exponent: [Ee]('-'?)[0-9][0-9]*;
FLOAT_LIT: INT_LIT Point INT_LIT? Exponent?
         | Point INT_LIT Exponent?
         | INT_LIT Exponent;


BOOL_LIT: TRUE | FALSE;

STRING_LIT: '"'~[\b\f\r\n\t\\]*'"';

