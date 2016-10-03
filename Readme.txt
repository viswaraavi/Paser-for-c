
No of non terminals:40
No of productions:90

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The grammer tried converted to LL(1)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<program>--><datadecls><funclist>

<funclist>-->empty|<func><funclist>

<func>--><funcdecl><funcprime>

<funcprime>-->semicolon|left_brace<datadecls><statements>right_brace

<funcdecl>--><typename>ID left_parenthesis<parameterlist>right_parenthesis

<typename>-->int|void|binary|decimal

<parameterlist>-->empty|void<parameter list prime>|int ID <non-emptylist>prime|binary ID<non-emptylist>prime|decimal ID<non-emptylist>prime

<parameter list prime> --> ID ID<non-emptylist>prime|empty

<non-emptylist>prime-->comma <non-emptylist>|empty

<non-emptylist>-->int ID <non-emptylist>prime|void ID<non-emptylist>prime|binary ID<non-emptylist>prime|decimal ID<non-emptylist>prime

<datadecls>-->empty|int<idlist> semicolon <datadecls>|void <idlist> semicolon<datadecls>|binary <idlist> semicolon <datadecls>|decimal<idlist>semicolon<datadecls>

<idlist>--><id><idlist>prime

<idlist>prime-->comma<id><idlist>prime|empty

<id>-->ID<id prime>

<id prime> -->empty|left_bracket<expression>right_bracket


<blockstatements>-->left_brace <statements>right_brace

<statements>-->empty|ID <statement prime><statements>|<ifstatement><statements>|<whilestatement><statements>|<returnstatement><statements>|<breakstatement><statements>|<continuestatement><statements>|readleft_parenthesis ID right_parenthesis semicolon<statements>|write left_parenthesis <expression> right_parenthesis semicolon<statements>|printleft_parenthesis STRING right_parenthesis semicolon<statements>

<statement prime> --> equal_sign <expression> semicolon| left_bracket <expression> right_bracket equal_sign<expression>semicolon|left_parenthesis <expr list> right_parenthesis semicolon 


<exprlist>-->empty|<non-emptyexprlist>

<non-emptyexprlist>--><expression><non-emptyexprlist>prime

<non-emptyexprlist>prime-->comma<expression><non-emptyexprlist>prime|empty




<ifstatement>-->if left_parenthesis<conditionexpression>right_parenthesis<blockstatements>

<conditionexpression>--><condition><condition expression prime>
<condition expression prime> --> empty|<conditionop><condition>

<conditionop>-->double_and_sign|double_or_sign

<condition>--><expression><condition prime>

<condition prime> --> <comparisonop><expression>

<comparisonop>-->==|!=|>|>=|<|<=


<whilestatement>-->while left_parenthesis<conditionexpression>right_parenthesis<blockstatements>

<returnstatement>-->return<expression>semicolon|return semicolon

<breakstatement>--->break semicolon

<continuestatement>--->continue semicolon


<expression>--><term><expression>prime

<expression>prime--><addop><term><expression>prime|empty

<addop>-->plus_sign|minus_sign

<term>--><factor><term>prime

<term>prime--><mulop><factor><term>prime|empty

<mulop>-->star_sign|forward_slash

<factor>-->ID<factor prime>|NUMBER|minus_sign NUMBER|left_parenthesis<expression>right_parenthesis

<factor prime> -->left_bracket<expression>right_bracket|left_parenthesis<exprlist>right_parenthesis|empty

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

How to compile the program?

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The program can be compiled as 

Python parser.py filename

filename can be file n current folder or the path name of the file

The output of program will be simmillar to following if its success

The program has been parsed sucessfully
Variables
9
Functions
3
Statements
127


If its a failure then it reports that the program is failure.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Program characterstics

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. First the grammer is converted ll1 grammer by the script that is submitted ll1grammer.py. The proogram is only left refactoring and left recursion is done by hand

2. The scanner is modified for our context by returing tokens with terminals

3.my implementation is nothing but a recursive decent algorithm. Where each production in grammer rule is converted to
The corrsoponding function. But at only data decls we have to look a head more than one token and take a decision whether it's
a data decleration or funclist

4. parser implements two methods getnexttoken() which parser consumes. lookaheadtoken() which parser looks at but does not consumes.
   so first parser looks at the token if it is appropriate it consumes or otherwise take descision based on it

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Potential bugs

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

This program currently runs for all input test cases. But since the implementation is with if and else the program has to be tested more test cases.
