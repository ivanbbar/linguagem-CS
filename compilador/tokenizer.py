import re

from tokens import Token
from tokens import PlusToken
from tokens import MinusToken
from tokens import MultToken
from tokens import DivToken
from tokens import AndToken
from tokens import OrToken
from tokens import NotToken
from tokens import EqualToken
from tokens import GTToken
from tokens import LTToken
from tokens import NumericToken
from tokens import EOFToken
from tokens import LeftParenToken
from tokens import RightParenToken
from tokens import PrintToken
from tokens import ReadToken
from tokens import AssignmentToken
from tokens import IdentifierToken
from tokens import EndToken
from tokens import BreakToken
from tokens import IfToken
from tokens import ElseToken
from tokens import WhileToken
from tokens import TypeToken
from tokens import StringToken
from tokens import VarDecToken
from tokens import DotToken
from tokens import FunctionToken
from tokens import ReturnToken
from tokens import CommaToken

class PrePro:

    @staticmethod
    def _remove_comments(code: str) -> str:
        return re.sub(r"#.*", "", code)

    @staticmethod
    def _remove_spaces_around_operators(code: str) -> str:
        return re.sub(r"\s*([+\-*/])\s*", r"\1", code)
    
    @staticmethod
    def add_eof(code: str) -> str: 
        return code + "\0"

    @staticmethod
    def preprocess(code: str) -> str:
        code = PrePro._remove_comments(code)
        code = PrePro._remove_spaces_around_operators(code)
        code = PrePro.add_eof(code)
        return code

map_knownnames = {
    "komunikar" : PrintToken,
    "kaptar" : ReadToken,
    "enquanto" : WhileToken,
    "kazo" : IfToken,
    "kazo_nao" : ElseToken,
    "Int": TypeToken,
    "String": TypeToken,
    "komprakatuaba": FunctionToken,
    "entregue": ReturnToken,
    "gole": EndToken
}

class Tokenizer():
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.next = None

    def check_next(self):
        next = self.next
        position = self.position
        current_char = self.source[self.position]

        # Skip any whitespace characters
        if (current_char.isspace() and current_char != "\n"):
            broom = position
            while broom < len(self.source) and (current_char.isspace() and current_char != "\n"):
                broom +=1
                if broom < len(self.source):
                    current_char = self.source[broom]
            position = broom

        # Check if the character is known
        if current_char.isalpha():
            if (current_char == "c"):
                raise Exception("'c' nao existe nessa linguagem")
            else:
                i = position
                token = current_char

                while i < len(self.source) and (current_char.isalnum() or current_char == '_'):
                    if (current_char == "c"):
                        raise Exception("'c' e 's' nao existe nessa linguagem")
                    else:
                        i += 1
                        if i < len(self.source):
                            current_char = self.source[i]
                            token += current_char

            token = token[:-1]
            position = i

            if token in map_knownnames.keys():
                if token == "Int":
                    next = map_knownnames[token]("Int")
                elif token == "String":
                    next = map_knownnames[token]("String")
                else:
                    next = map_knownnames[token]()
            else:
                next = IdentifierToken(value=token)

        elif current_char == '"':
            position += 1
            current_char = self.source[position]
            if (current_char == "c"):
                raise Exception("'c' existe nessa linguagem")
            else:
                broom = position
                token = current_char
                while broom < len(self.source) and (current_char != '"'):
                    broom += 1
                    if broom < len(self.source):
                        current_char = self.source[broom]
                        if (current_char == "c" or current_char == "s"):
                            raise Exception("'c' e 's' não exiztem nexa linguagem")
                        else:
                            token += current_char
                token = token[:-1]
                position = broom+1

                next = StringToken(token)

        elif current_char == "\n":
            next = BreakToken()
            position += 1
        
        # Check if the character is a digit
        elif current_char.isdigit():
            # Read in the entire integer value
            num_str = ""
            token = current_char
            broom = position
            while (token.isdigit() and broom < len(self.source)):
                num_str += token
                broom += 1
                if broom < len(self.source):
                    token = self.source[broom]
            position = broom
            next = NumericToken(int(num_str))

        # Check if the character is an equal sign
        elif current_char == "=":
            if position + 1 < len(self.source) and self.source[position + 1] == "=":
                next = EqualToken()
                position += 2
            else:
                next = AssignmentToken()
                position += 1
        # Check if the character is a plus sign
        elif current_char == "+":
            next = PlusToken()
            position += 1
        # Check if the character is a minus sign
        elif current_char == "-":
            next = MinusToken()
            position += 1
        # Check if the character is a mult sign        
        elif current_char == "*":
            next = MultToken()
            position += 1
        # Check if the character is a div sign
        elif current_char == "/":
            next = DivToken()
            position += 1
        # Check if the character is a left parenthesis
        elif current_char == "(":
            next = LeftParenToken()
            position += 1
        # Check if the character is a right parenthesis
        elif current_char == ")":
            next = RightParenToken()
            position += 1
        # Check if the character is a not
        elif current_char == "!":
            next = NotToken()
            position += 1
        # Check if the character is a >
        elif current_char == ">":
            next = GTToken()
            position += 1          
        # Check if the character is a <
        elif current_char == "<":
            next = LTToken()
            position += 1      
        elif current_char == '.':
            next = DotToken()
            position += 1
        elif current_char == ',':
            next = CommaToken()
            position += 1
        # Check if the character is an & sign
        elif current_char == "&":
            if position + 1 < len(self.source) and self.source[position + 1] == "&":
                next = AndToken()
                position += 2
            else:
                raise Exception("Ivanlid Syntax")
        # Check if the character is an : sign
        elif current_char == ":":
            if position + 1 < len(self.source) and self.source[position + 1] == ":":
                next = VarDecToken()
                position += 2
            else:
                raise Exception("Ivanlid Syntax")
        # Check if the character is an | sign
        elif current_char == "|":
            if position + 1 < len(self.source) and self.source[position + 1] == "|":
                next = OrToken()
                position += 2
            else:
                raise Exception("Ivanlid Syntax")
        # Check if we've reached the end of the input string        
        elif current_char == "\0":
            next = EOFToken()

        else:
            # If the character is not a plus, minus, digit, or parenthesis, raise an error
            raise TypeError('Invalid character')

    #    print(f'next -> {next.value}')
        return next, position
    
    def select_next(self):
        self.next, self.position = self.check_next()