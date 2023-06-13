class Token:
    def __init__(self, value):
        self.value = value
    
    def _value(self):
        ...
    
class OperatorToken(Token):
    def __init__(self, value):
        super().__init__(value)

class AndToken(OperatorToken):
    def __init__(self):
        super().__init__("&&")

    @property
    def _value(self):
        return "and"

class AssignmentToken(Token):
    def __init__(self):
        super().__init__("=")

    @property
    def _value(self):
        return "assignment"


class BracketToken(Token):
    def __init__(self, value) -> None:
        super().__init__(value)

class BreakToken(Token):
    def __init__(self):
        super().__init__("\n")

    @property
    def _value(self):
        return "break"

class ColonToken(Token):
    def __init__(self):
        super().__init__(":")

    @property
    def _value(self):
        return "colon"

class CommaToken(Token):
    def __init__(self):
        super().__init__(",")

    @property
    def _value(self):
        return "comma"

class ConditionalToken(Token):
    def __init__(self, value):
        super().__init__(value)

class DivToken(OperatorToken):
    def __init__(self):
        super().__init__("/")

    @property
    def _value(self):
        return "div"

class DotToken(Token):
    def __init__(self):
        super().__init__(".")

    @property
    def _value(self):
        return "dot"

class EOFToken(Token):
    def __init__(self):
        super().__init__("\0")

    @property
    def _value(self):
        return "eof"

class ElseToken(ConditionalToken):
    def __init__(self):
        super().__init__("kazo_nao")

    @property
    def _value(self):
        return "else"

class FunctionToken(Token):
    def __init__(self):
        super().__init__("komprakatuaba")

    @property
    def _value(self):
        return "function"

class EqualToken(OperatorToken):
    def __init__(self):
        super().__init__("==")

    @property
    def _value(self):
        return "equal"

class FuncToken(Token):
    def __init__(self, value):
        super().__init__(value)

class EndToken(FuncToken):
    def __init__(self):
        super().__init__("gole")

    @property
    def _value(self):
        return "end"

class GTToken(OperatorToken):
    def __init__(self):
        super().__init__(">")

    @property
    def _value(self):
        return "gt"

class IdentifierToken(Token):
    def __init__(self, value=None):
        super().__init__(value)

    @property
    def _value(self):
        return "identifier"

class IfToken(ConditionalToken):
    def __init__(self):
        super().__init__("kazo")

    @property
    def _value(self):
        return "if"

class LTToken(OperatorToken):
    def __init__(self):
        super().__init__("<")

    @property
    def _value(self):
        return "lt"

class ParenToken(Token):
    def __init__(self,value):
        super().__init__(value)

class LeftParenToken(ParenToken):
    def __init__(self):
        super().__init__("(")
    
    @property
    def _value(self):
        return "left parenthesis"

class LoopToken(Token):
    def __init__(self, value):
        super().__init__(value)

class MinusToken(OperatorToken):
    def __init__(self):
        super().__init__("-")

    @property
    def _value(self):
        return "minus"

class MultToken(OperatorToken):
    def __init__(self):
        super().__init__("*")

    @property
    def _value(self):
        return "mult"

class NotToken(OperatorToken):
    def __init__(self):
        super().__init__("!")

    @property
    def _value(self):
        return "not"

class NumericToken(Token):
    def __init__(self, value: int):
        super().__init__(value)

    @property
    def _value(self):
        return "numeric"

class OrToken(OperatorToken):
    def __init__(self):
        super().__init__("||")

    @property
    def _value(self):
        return "or"

class PlusToken(OperatorToken):
    def __init__(self):
        super().__init__("+")

    @property
    def _value(self):
        return "plus"


class PrintToken(FuncToken):
    def __init__(self):
        super().__init__("komunikar")

    @property
    def _value(self):
        return "println"

class ReadToken(FuncToken):
    def __init__(self):
        super().__init__("kaptar")

    @property
    def _value(self):
        return "readline"

class ReturnToken(Token):
    def __init__(self):
        super().__init__("entregue")

    @property
    def _value(self):
        return "return"

class RightParenToken(ParenToken):
    def __init__(self):
        super().__init__(")")
    
    @property
    def _value(self):
        return "right parenthesis"

class StringToken(Token):
    def __init__(self, value):
        super().__init__(value)

    @property
    def _value(self):
        return "string"

class TypeToken(Token):
    def __init__(self, value):
        super().__init__(value)

    @property
    def _value(self):
        return "type"

class VarDecToken(Token):
    def __init__(self):
        super().__init__("variavel")

    @property
    def _value(self):
        return "var dec"

class WhileToken(LoopToken):
    def __init__(self):
        super().__init__("enquanto")

    @property
    def _value(self):
        return "while"