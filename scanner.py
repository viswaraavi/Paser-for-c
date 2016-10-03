import re
import sys



class Token:
    """ This implements the token langauge"""

    int="int"
    void="void"
    binary="binary"
    decimal="decimal"
    while1="while"
    if1="if"
    return1="return"
    read1="read"
    write="write"
    break1="break"
    continue1="continue"
    print1='print'
    Number = "NUMBER"
    Identifier = "ID"
    Symbol = "<Symbol>"
    String = "STRING"
    Metasyntax = "metasyntax"
    doubleequalto="=="
    notequalto= "!="
    greater=">"
    lesser="<"
    greater1=">="
    lesser1="<="
    semicolon="semicolon"
    comma="comma"
    left="left_paranthesis"
    right="right_paranthesis"
    leftb="left_brace"
    rightb="right_brace"
    leftbra="left_bracket"
    rightbra="right_bracket"
    andsign="double_and_sign"
    equal="equal_sign"
    orsign="double_or_sign"
    plus="plus_sign"
    minus="minus_sign"
    star="star_sign"
    slash="forward_slash"
    eof=None


    regexp = [
        (int,"int"),
        (void,"void"),
        (binary,"binary"),
        (decimal,"decimal"),
        (while1, "while"),
        (if1, "if"),
        (return1, "return"),
        (read1, "read"),
        (write, "write"),
        (break1, "break"),
        (continue1, "continue"),
        (print1,"print"),
        (Number, "[0-9]+"),
        (Identifier, "[a-zA-Z_]([a-zA-Z_]|[0-9])*"),
        (doubleequalto,"=="),
        (notequalto,"!="),
        (greater,">"),
        (lesser,"<"),
        (greater1,">="),
        (lesser1,"<="),
        (left,'\('),
        (right,'\)'),
        (leftb,'\{'),
        (rightb,'\}'),
        (leftbra,'\['),
        (rightbra,'\]'),
        (andsign,'\&\&'),
        (orsign,'\|\|'),
        (equal,'\='),
        (semicolon,'\;'),
        (comma,'\,'),
        (plus,'\+'),
        (minus,'-'),
        (star,'\*'),
        (slash,'\/'),
        (String, '\".*\"'),
        (Metasyntax, "(#.*\n)|((//.*\n))")


    ]


class Scanner:
    """ This implements the scanner that is need to tokneize the string"""

    def __init__(self, string):
        self.input_string = string
        self.current_char = 0
        self.current_token = (None, '')

    def skip_white_space(self):
        if (self.current_char >= len(self.input_string) - 1):
            return
        while self.current_char <= len(self.input_string) - 1 and self.input_string[self.current_char].isspace():
            self.current_char += 1

    def get_current_token(self):
        self.skip_white_space()
        token, longest = None, ''
        for (t, r) in Token.regexp:
            match = re.match(r, self.input_string[self.current_char:])
            if match and match.end() > len(longest):
                token, longest = t, match.group()
        self.current_char = self.current_char + len(longest)
        if (token):
            return (token, longest)
        else:
            self.current_char = self.current_char + 1
            return (None,"")

    def peektoken(self):
        temp=self.current_char
        token1,longest1=self.get_current_token()
        token2, longest2 = self.get_current_token()
        token3, longest3 = self.get_current_token()
        self.current_char=temp
        return [(token1,longest1),(token2,longest2),(token3,longest3)]

    def peektoken1(self):
        self.skip_white_space()
        token, longest = None, ''
        for (t, r) in Token.regexp:
            match = re.match(r, self.input_string[self.current_char:])
            if match and match.end() > len(longest):
                token, longest = t, match.group()
        if (token):
            return (token, longest)
        else:
            self.current_char=self.current_char+1
            return (None, "")





    def isnexttoken(self):
        if (self.current_char >= len(self.input_string)):
            return False
        else:
            return True

    def getnexttoken(self):
        if (self.isnexttoken()):
            self.current_token = self.get_current_token()
            return self.current_token
        else:
            self.current_char=self.current_char+1
            return (Token.eof, "")









