

import scanner
import sys

"""
Our implementation is nothing but a recursive decent algorithm. Where each production in grammer rule is converted to
The corrsoponding function. But at only data decls we have to look a head more than one token and take a decision whether it's
a data decleration or funclist
"""


class Parser:
    def __init__(self,string):
        self.scanner_obj=scanner.Scanner(string)
        self.current_token=None
        self.numvar=0
        self.numfunc=0
        self.numstate=0

    #This method consumes the token
    def getnexttoken(self):
        token=self.scanner_obj.getnexttoken()
        while(token[0] == scanner.Token.Metasyntax):
            token = self.scanner_obj.getnexttoken()
        self.current_token=token
        return self.current_token

    #this method just looks into the token without consumption
    def peeknexttoken(self):
        token = self.scanner_obj.peektoken()
        self.current_token = token
        return self.current_token

    #this method returns tokens a head by 3 times. This is because the grammer we have is not ll[1]
    #because the first and follow sets of data decls overlap so we have to look a head more than once to determine what to do
    def lookahead(self):
        while (self.scanner_obj.peektoken1()[0]==scanner.Token.Metasyntax):
            token = self.scanner_obj.getnexttoken()
        self.current_token = self.scanner_obj.peektoken1()
        return self.current_token




    def program(self):
        if(self.data_decls()):
            if(self.func_list()):
                if(self.current_token[0]==scanner.Token.eof):
                    return True
                else:
                    return False
            else:
                return False

        else:
            return False

    def func_list(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.eof):
            return True
        else:
            if(self.func()):
                return self.func_list()

    def func(self):
        if(self.func_decl()):
            if(self.func_prime()):
                return True
            else:
                return False

        else:
            return False

    def func_decl(self):
        if(self.typename()):
            self.lookahead()
            if(self.current_token[0]==scanner.Token.Identifier):
                self.getnexttoken()
                self.lookahead()
                if(self.current_token[0]==scanner.Token.left):
                    self.getnexttoken()
                    if(self.parameter_list()):
                        self.lookahead()
                        if(self.current_token[0]==scanner.Token.right):
                            self.getnexttoken()
                            return True

        return False


    def func_prime(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.semicolon):
            self.getnexttoken()
            return True
        else:
            if(self.current_token[0]==scanner.Token.leftb):
                self.getnexttoken()
                if(self.data_decls()):
                    if(self.statements()):
                        self.lookahead()
                        if(self.current_token[0]==scanner.Token.rightb):
                            self.numfunc=self.numfunc+1
                            self.getnexttoken()

                            return True

        return False

    def typename(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.int or scanner.Token.void or scanner.Token.binary or scanner.Token.decimal):
            self.getnexttoken()
            return True

        return False

    def parameter_list(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.void):
            self.getnexttoken()
            if(self.parameter_list_prime()):
                return True

            else:
                return False
        if(self.current_token[0] in (scanner.Token.int,scanner.Token.binary,scanner.Token.decimal)):
            self.getnexttoken()
            self.lookahead()
            if(self.current_token[0]==scanner.Token.Identifier):
                self.getnexttoken()
                if(self.non_empty_prime()):
                    return True
                else:
                    return False
            else:
                return False


        return True


    def parameter_list_prime(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.right):
            return True
        else:
            if(self.current_token[0]==scanner.Token.Identifier):
                self.getnexttoken()
                if(self.non_empty_prime()):
                    return True

        return False

    def non_empty_prime(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.comma):
            self.getnexttoken()
            if(self.non_empty()):
                return True
            else:
                return False

        return True

    def non_empty(self):
        self.lookahead()
        if(self.current_token[0] in (scanner.Token.int,scanner.Token.void,scanner.Token.decimal,scanner.Token.binary)):
            self.getnexttoken()
            self.lookahead()
            if(self.current_token[0]==scanner.Token.Identifier):
                self.getnexttoken()
                if(self.non_empty_prime()):
                    return True
        return False


    def data_decls(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.eof):
            return True
        if(self.current_token[0] in (scanner.Token.int,scanner.Token.void,scanner.Token.binary,scanner.Token.decimal)):

            list1=self.peeknexttoken()
            token1=list1[1]
            token2=list1[2]
            if(token1[0]==scanner.Token.Identifier and token2[0]==scanner.Token.left):
                self.current_token=None
                return True
            self.getnexttoken()
            if(self.idlist()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.semicolon):
                    self.getnexttoken()
                    return self.data_decls()
                else:
                    return False
            else:
                return False

        return True




    def idlist(self):
        if(self.id()):
            if(self.idlist_prime()):
                return True
        else:
            return False


    def idlist_prime(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.comma):
            self.getnexttoken()
            if(self.id()):
                if(self.idlist_prime()):
                    return True
                else:
                    return False
            else:
                return False

        return True


    def id(self):
        self.getnexttoken()
        if(self.current_token[0]==scanner.Token.Identifier):
            self.numvar=self.numvar+1
            if(self.idprime()):
                return True
        return False

    def idprime(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.leftbra):
            self.getnexttoken()
            if(self.expression()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.rightbra):
                    self.getnexttoken()
                    return True
                else:
                    return False
            else:
                return False


        return True

    def block_statements(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.leftb):
            self.getnexttoken()
            if(self.statements()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.rightb):
                    self.getnexttoken()
                    return True

        return False


    def statements(self):

        if(self.ifstatement() or self.whilestatement() or self.returnstatement() or self.breakstatement() or self.continuestatement()):
            self.numstate=self.numstate+1
            return self.statements()
        self.lookahead()
        if(self.current_token[0]==scanner.Token.Identifier):
            self.getnexttoken()
            if(self.statementprime()):
                self.numstate=self.numstate+1
                if(self.statements()):
                    return True
                else:
                    return False
            else:
                return False

        if(self.current_token[0] in (scanner.Token.read1,scanner.Token.write) ):
            self.getnexttoken()
            self.lookahead()
            if(self.current_token[0]==scanner.Token.left):
                self.getnexttoken()
                if(self.expression()):
                    self.lookahead()
                    if(self.current_token[0]==scanner.Token.right):
                        self.getnexttoken()
                        self.lookahead()
                        if(self.current_token[0]==scanner.Token.semicolon):
                            self.getnexttoken()
                            self.numstate=self.numstate+1
                            if(self.statements()):
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False



        if (self.current_token[0] ==scanner.Token.print1):
            self.getnexttoken()
            self.lookahead()
            if (self.current_token[0] == scanner.Token.left):
                self.getnexttoken()
                self.lookahead()
                if (self.current_token[0] == scanner.Token.String):
                    self.getnexttoken()
                    self.lookahead()
                    if (self.current_token[0] == scanner.Token.right):
                        self.getnexttoken()
                        self.lookahead()
                        if (self.current_token[0] == scanner.Token.semicolon):
                            self.getnexttoken()
                            self.numstate=self.numstate+1
                            if (self.statements()):
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False


        return True



    def statementprime(self):
        self.lookahead()
        if(self.current_token[0] ==scanner.Token.equal):
            self.getnexttoken()
            if(self.expression()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.semicolon):
                    self.getnexttoken()
                    return True

        if(self.current_token[0]==scanner.Token.leftbra):
            self.getnexttoken()
            if(self.expression()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.rightbra):
                    self.getnexttoken()
                    self.lookahead()
                    if (self.current_token[0] == scanner.Token.equal):
                        self.getnexttoken()
                        if(self.expression()):
                            self.lookahead()
                            if(self.current_token[0]==scanner.Token.semicolon):
                                self.getnexttoken()
                                return True






        if(self.current_token[0]==scanner.Token.left):
            self.getnexttoken()
            if(self.expr_list()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.right):
                    self.getnexttoken()
                    self.lookahead()
                    if(self.current_token[0]==scanner.Token.semicolon):
                        self.getnexttoken()
                        return True
        return False


    def expr_list(self):
        if (self.expression()):
            if (self.nonemptyexpressprime()):
                return True
            else:
                return False
        return True



    def nonemptyexpressprime(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.comma):
            self.getnexttoken()
            if(self.expression()):
                if(self.nonemptyexpressprime()):
                    return True
                else:
                    return False
            else:
                return False

        return True

    def ifstatement(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.if1):
            self.getnexttoken()
            self.lookahead()
            if(self.current_token[0]==scanner.Token.left):
                self.getnexttoken()
                if(self.conditionexpression()):
                    self.lookahead()
                    if(self.current_token[0]==scanner.Token.right):
                        self.getnexttoken()
                        if(self.block_statements()):
                            return True
        return False


    def conditionexpression(self):
        if(self.condition()):
            if(self.conditionexpressionprime()):
                return True

        return False

    def conditionexpressionprime(self):
        if(self.conditionop()):
            if(self.condition()):
                return True
            else:
                return False

        return True


    def condition(self):
        if(self.expression()):
            if(self.condition_prime()):
                return True
        return False

    def condition_prime(self):
        if(self.comparisionop()):
            if(self.expression()):
                return True
        return False

    def conditionop(self):
        self.lookahead()
        if(self.current_token[0] in (scanner.Token.andsign ,scanner.Token.orsign)):
            self.getnexttoken()
            return True
        return False

    def comparisionop(self):
        self.getnexttoken()
        if(self.current_token[0] in (scanner.Token.doubleequalto,scanner.Token.notequalto,scanner.Token.greater,scanner.Token.greater1,scanner.Token.lesser,scanner.Token.lesser1)):
            return True
        return False


    def whilestatement(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.while1):
            self.getnexttoken()
            self.lookahead()
            if(self.current_token[0]==scanner.Token.left):
                self.getnexttoken()
                if(self.conditionexpression()):
                    self.lookahead()
                    if(self.current_token[0]==scanner.Token.right):
                        self.getnexttoken()
                        if(self.block_statements()):
                            return True
        return False

    def returnstatement(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.return1):
            self.getnexttoken()
            self.lookahead()
            if (self.current_token[0] == scanner.Token.semicolon):
                self.getnexttoken()
                return True
            if(self.expression()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.semicolon):
                    self.getnexttoken()
                    return True

        return False



    def breakstatement(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.break1):
            self.getnexttoken()
            self.lookahead()
            if(self.current_token[0]==scanner.Token.semicolon):
                self.getnexttoken()
                return True
        return False

    def continuestatement(self):
        self.lookahead()
        if (self.current_token[0] == scanner.Token.continue1):
            self.getnexttoken()
            self.lookahead()
            if (self.current_token[0] == scanner.Token.semicolon):
                self.getnexttoken()
                return True
        return False

    def expression(self):
        if(self.term()):
            if(self.expression_prime()):
                return True
        return False

    def expression_prime(self):
        if(self.add_op()):
            if(self.term()):
                if(self.expression_prime()):
                    return True
                else:
                    return False
            else:
                return False

        return True

    def add_op(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.plus or self.current_token[0]==scanner.Token.minus):
            self.getnexttoken()
            return True

    def term(self):
        if(self.factor()):
            if(self.term_prime()):
                return True
        return False

    def term_prime(self):
        if(self.mulop()):
            if(self.factor()):
                if(self.term_prime()):
                    return True
                else:
                    return False
            else:
                return False

        return True

    def mulop(self):
        self.lookahead()
        if (self.current_token[0] == scanner.Token.star or self.current_token[0] == scanner.Token.slash):
            self.getnexttoken()
            return True

    def factor(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.Identifier):
            self.getnexttoken()
            if(self.factor_prime()):
                return True
        if (self.current_token[0] == scanner.Token.Number):
            self.getnexttoken()
            return True
        if(self.current_token[0] == scanner.Token.minus):
            self.getnexttoken()
            self.lookahead()
            if (self.current_token[0] == scanner.Token.Number):
                self.getnexttoken()
                return True
        if (self.current_token[0]==scanner.Token.left):
            self.getnexttoken()
            if(self.expression()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.right):
                    self.getnexttoken()
                    return True

        return False




    def factor_prime(self):
        self.lookahead()
        if(self.current_token[0]==scanner.Token.leftbra):
            self.getnexttoken()
            if(self.expression()):
                self.lookahead()
                if(self.current_token[0]==scanner.Token.rightbra):
                    self.getnexttoken()
                    return True
                else:
                    return False
            else:
                return False
        if (self.current_token[0] == scanner.Token.left):
            self.getnexttoken()
            if (self.expr_list()):
                self.lookahead()
                if (self.current_token[0] == scanner.Token.right):
                    self.getnexttoken()
                    return True
                else:
                    return False
            else:
                return False



        return True



fullpath=sys.argv[1]
file = open(fullpath, 'r')
content=file.read()
parser=Parser(content)
bool1=parser.program()
if(bool1):
    print "The program has been parsed sucessfully"
    print "Variables"
    print parser.numvar
    print "Functions"
    print parser.numfunc
    print "Statements"
    print parser.numstate
else:
    print parser.scanner_obj.input_string[parser.scanner_obj.current_char:]
    print "The program has errors check your errors"



























































