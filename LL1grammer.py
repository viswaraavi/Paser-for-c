import random
grammer="""<program> --> <data decls> <func list>
<func list> --> empty | <func> <func list>
<func> --> <func decl> semicolon | <func decl> left_brace <data decls> <statements> right_brace
<func decl> --> <type name> ID left_parenthesis <parameter list> right_parenthesis
<type name> --> int | void | binary | decimal
<parameter list> --> empty | void | <non-empty list>
<non-empty list> --> <type name> ID | <non-empty list> comma <type name> ID
<data decls> --> empty | <type name> <id list> semicolon <data decls>
<id list> --> <id> | <id list> comma <id>
<id> --> ID | ID left_bracket <expression> right_bracket
<block statements> --> left_brace <statements> right_brace
<statements> --> empty | <statement> <statements>
<statement> --> <assignment> | <func call> | <if statement> | <while statement> | <return statement> | <break statement> | <continue statement> | read left_parenthesis  ID right_parenthesis semicolon | write left_parenthesis <expression> right_parenthesis semicolon | print left_parenthesis  STRING right_parenthesis semicolon
<assignment> --> <id> equal_sign <expression> semicolon
<func call> --> ID left_parenthesis <expr list> right_parenthesis semicolon
<expr list> --> empty | <non-empty expr list>
<non-empty expr list> --> <expression> | <non-empty expr list> comma <expression>
<if statement> --> if left_parenthesis <condition expression> right_parenthesis <block statements>
<condition expression> -->  <condition> | <condition> <condition op> <condition>
<condition op> --> double_and_sign | double_or_sign
<condition> --> <expression> <comparison op> <expression>
<comparison op> --> == | != | > | >= | < | <=
<while statement> --> while left_parenthesis <condition expression> right_parenthesis <block statements>
<return statement> --> return <expression> semicolon | return semicolon
<break statement> ---> break semicolon
<continue statement> ---> continue semicolon
<expression> --> <term> | <expression> <addop> <term>
<addop> --> plus_sign | minus_sign
<term> --> <factor> | <term> <mulop> <factor>
<mulop> --> star_sign | forward_slash
<factor> --> ID | ID left_bracket <expression> right_bracket | ID left_parenthesis <expr list> right_parenthesis | NUMBER | minus_sign NUMBER | left_parenthesis <expression> right_parenthesis"""


grammer_list=grammer.split("\n")
dict1={}
non_terminals=[]
for element in grammer_list:
    subelement= element.split("-->")
    subelement[0]="".join(subelement[0].split())
    subelement[1]="".join(subelement[1].split())
    subelement[1]=subelement[1].split("|")
    non_terminals.append(subelement[0])
    dict1[subelement[0]]=subelement[1]






def replace_production(non_terminal1,non_terminal2):
    list_productions=dict1[non_terminal1]
    for index in range(len(list_productions)):
        index_str=list_productions[index].find(non_terminal2)
        if(index_str==0):
            counter=0
            rep_prod=list_productions[index]
            for element in dict1[non_terminal2]:
                if(counter==0):
                    list_productions[index]=list_productions[index].replace(non_terminal2,element)
                    counter=counter+1
                else:
                    list_productions.append(rep_prod.replace(non_terminal2,element))


def eliminate_left_recursion(nonterminal):
    list_productions=dict1[nonterminal]
    bool1=False
    new_list=[]
    for index in range(len(list_productions)):
        index_str=list_productions[index].find(nonterminal)
        if(index_str==0):
            bool1=True
            for index1 in range(len(list_productions)):
                if(nonterminal not in list_productions[index1]):
                    list_productions[index1]=list_productions[index1]+(nonterminal+"prime")
                    new_list.append(list_productions[index1])
            break
        else:
            continue
    if(bool1):
        dict1[nonterminal+"prime"]=[]
        for index in range(len(list_productions)):
            index_str = list_productions[index].find(nonterminal)
            if (index_str == 0):
                list_productions[index]=list_productions[index].replace(nonterminal,"",1)
                dict1[nonterminal + "prime"].append(list_productions[index]+nonterminal+"prime")
            if(nonterminal in list_productions[index] and index_str!=0 and list_productions[index][index_str+len(nonterminal)]!='p' and list_productions[index][index_str+len(nonterminal)+2]!='r' and list_productions[index][index_str+len(nonterminal)+3]!='i' and list_productions[index][index_str+4+len(nonterminal)]!='m'  ):
                list_productions[index]=list_productions[index] + (nonterminal + "prime")
                new_list.append(list_productions[index])
        dict1[nonterminal+"prime"].append("epsilon")
        dict1[nonterminal]=new_list


def leftrecursive():
    for i in range(len(non_terminals)):
        for j in range(len(non_terminals[:i])):
            replace_production(non_terminals[i],non_terminals[j])

        eliminate_left_recursion(non_terminals[i])

leftrecursive()

for element in dict1.items():
    element=list(element)
    element[1]="|".join(element[1])
    element="-->".join(element)
    print element



