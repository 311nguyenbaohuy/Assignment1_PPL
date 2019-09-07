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

// program  : many_decls? mctype 'main' LB RB LP body? RP EOF ;
program  : many_decls? mctype 'main' LB RB block_stmt EOF ;


// body: funcall SEMI;
body    
            : (stmt)+
            ;

// exp: funcall | INTLIT ;

// funcall: ID LB exp? RB ;

LB: '(' ;

RB: ')' ;

LSB: '[';

RSB: ']';

LP: '{';

RP: '}';

SEMI: ';' ;

COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: [?~`@#$^:\\.'];
UNCLOSE_STRING: '"' ('\\' [bfrnt"\\] | ~[\b\f\r\n\t\\"])*;
ILLEGAL_ESCAPE: '"' ('\\'~[bfnrt"] | ~'\\')*;

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

STRINGLIT: '"'('\\' [bfrnt"\\] | ~[\b\f\r\n\t\\"])*'"';

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

lit         
            : INTLIT 
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

mctype
            : primary_type
            | VOIDTYPE
            | output_ptr_type
            ;



// Chua xet truong hop int a [0]
// con TH int a [b]
input_ptr_type
            : primary_type element
            ;

output_ptr_type
            : primary_type LSB RSB
            ;

element
            : ID LSB INTLIT RSB
            ;


many_decls 
            : decl (decl)*
            ;

decl
            : var_decl 
            | func_decl
            ;

var_decl
            : primary_type many_vars SEMI;

many_vars    
            : var (COMMA var)*;

var 
            : ID 
            | element
            ;            

func_decl
            : mctype ID LB list_params RB block_stmt
            ;

list_params
            : (param_decl (COMMA param_decl)*)?
            ;

param_decl  
            : primary_type ID
            | primary_type ID LSB RSB
            ;

call_func
            : ID LB list_exprs RB
            ;

list_exprs
            : (expr (COMMA expr)*)?
            ;

func_stmt  
            : call_func SEMI
            ;

if_stmt
            : match_stmt 
            | unmatch_stmt
            ;

match_stmt 
            : IF LB expr RB match_stmt ELSE match_stmt
            | other 
            ;

unmatch_stmt
            : IF LB expr RB match_stmt ELSE unmatch_stmt
            | IF LB expr RB stmt
            | other
            ;

do_while_stmt
            : DO (stmt)+ WHILE expr SEMI
            ; 

for_stmt
            : FOR LB expr SEMI expr SEMI expr RB stmt
            ;

break_stmt
            : BREAK SEMI
            ;

continue_stmt
            : CONTINUE SEMI
            ;

// return_void
//             : RETURN SEMI
//             ;

// return_expr
//             : RETURN expr SEMI
//             ;

return_stmt
            : RETURN expr? SEMI
            ;

expr_stmt
            : expr SEMI
            ;   

other       
            : func_stmt
            | var_decl      
            | do_while_stmt
            | for_stmt
            | break_stmt
            | continue_stmt
            | return_stmt
            | expr_stmt
            ;

stmt
            : other
            | if_stmt       
            ;

block_stmt
            : LP (stmt|block_stmt)* RP
            ;
expr   
            : LB expr RB 
            | expr1 LSB expr1 RSB
            | expr1
            ;
expr1
            : <assoc=right>SUB_OP expr1
            | NOT_OP expr1
            | expr1 DIV_OP expr1
            | expr1 MUL_OP expr1
            | expr1 MODULUS_OP expr1
            | expr1 ADD_OP expr1
            | expr1 SUB_OP expr1
            | expr2 LESS_EQUAL_OP expr2
            | expr2 LESS_OP expr2
            | expr2 GREATER_EQUAL_OP expr2
            | expr2 GREATER_OP expr2
            | expr2 EQUAL_OP expr2
            | expr2 NOT_EQUAL_OP expr2
            | expr2
            ;

expr2   
            : expr2 AND_OP expr2
            | expr2 OR_OP expr2
            | <assoc=right> expr2 ASSIGN_OP expr
            | op
            ;
op          
            : call_func
            | lit 
            | ID 
            | element;  



// chua check TH (-a + b + (a + 1)) va { stmt { stmt} stmt }