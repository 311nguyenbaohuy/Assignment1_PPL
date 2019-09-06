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

LB: '(' ;

RB: ')' ;

LSB: '[';

RSB: ']';

LP: '{';

RP: '}';

SEMI: ';' ;

COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;

// Comment

LINE_COMMENT: '//'~[\n\r]* -> skip;
BLOCK_COMMENT: '/*'(.)*?'*/'-> skip;
        

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

NOT_OP: '!';

OR_OP: '||';

NOT_EQUAL_OP: '!=';

LESS_OP: '<';

LESS_EQUAL_OP: '<=';

ASSIGN_OP: '=';

SUB_OP: '-';

MODULUS_OP: '%';

DIV_OP: '/';

AND_OP: '&&';

EQUAL_OP: '==';

GREATER_OP: '>';

GREATER_EQUAL_OP: '>=';

// Literals


INTLIT: [0-9]+;


fragment Point: '.';
fragment Exponent: [Ee]('-'?)[1-9][0-9]*;
FLOATLIT
            : INTLIT Point INTLIT? Exponent?
            | Point INTLIT Exponent?
            | INTLIT Exponent
            ;


BOOLLIT
            : TRUE 
            | FALSE
            ;

STRINGLIT: '"'~[\b\f\r\n\t\\"]*'"';

lit         : INTLIT 
            | FLOATLIT 
            | BOOLLIT 
            | STRINGLIT
            ;

primary_type
            : BOOLEANTYPE 
            | INTTYPE 
            | FLOATTYPE 
            | STRINGTYPE
            ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

// Chua xet truong hop int a [0]
input_ptr_type
            : primary_type ID LSB INTLIT RSB
            ;

output_ptr_type
            : primary_type ID LSB RSB
            ;

element
            : ID LSB INTLIT RSB
            ;

// Chua xet truong hop int a [0]
decl_var
            : primary_type ID SEMI
            | input_ptr_type SEMI
            ;
 
expr   
            : LB expr RB 
            | <assoc=right>SUB_OP expr
            | NOT_OP expr
            | expr DIV_OP expr
            | expr MUL_OP expr
            | expr MODULUS_OP expr
            | expr ADD_OP expr
            | expr SUB_OP expr
            | expr1 LESS_EQUAL_OP expr1
            | expr1 LESS_OP expr1
            | expr1 GREATER_EQUAL_OP expr1
            | expr1 GREATER_OP expr1
            | expr1 EQUAL_OP expr1
            | expr1 NOT_EQUAL_OP expr1
            | expr1
            ;

expr1
            : expr1 AND_OP expr1
            | expr1 OR_OP expr1
            | <assoc=right> expr1 ASSIGN_OP expr
            | op
            ;
op          
            : funcall 
            | lit 
            | ID 
            | element;  