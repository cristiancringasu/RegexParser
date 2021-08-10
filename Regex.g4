 grammar Regex;
 
 /*
    Regex grammar
  */
  
KLEEN : '*' ;
UNION : '|' ;
OPEN : '(' ;
CLOSE : ')' ;

WHITESPACE : [ \t\r\n]+ -> skip ;

VAR : [a-z] ;

expr : simple_expr | expr UNION simple_expr ;
simple_expr : basic_expr | simple_expr basic_expr;
basic_expr : atom KLEEN+ | atom ;
atom : variable | inner_expr ;
variable : VAR ;
inner_expr : OPEN expr CLOSE ;
