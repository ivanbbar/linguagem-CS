from datax import List, Variable, Function
from tablesx import SymbolTable
from tablesx import function_table

class Node:
    def __init__(self, value):
        self.value = value
        self.children = List(self)

    def evaluate(self, symbol_table):
        ...

class AssignNode(Node):
    def __init__(self):
        super().__init__("=")

    def evaluate(self, symbol_table):
        variable_name = self.children[0].value
        variable_value = self.children[1].evaluate(symbol_table)

        symbol_table.assign(variable_name, variable_value)

class BinOp(Node):
    def __init__(self, value):
        super().__init__(value)
    
    def evaluate(self, symbol_table):
        left = self.children[0].evaluate(symbol_table)
        right = self.children[1].evaluate(symbol_table)

        if self.value == "+":
            return left + right
        elif self.value == "-":
            return left - right
        elif self.value == "*":
            return left * right
        elif self.value == "/":
            return left // right
        elif self.value == '&&':
            return left and right
        elif self.value == '||':
            return left or right
        elif self.value == '==':
            return left == right
        elif self.value == '>':
            return left > right
        elif self.value == '<':
            return left < right
        elif self.value == '.':
            return left.__concat__(right)
        raise SyntaxError("error on arithmetic operation")

class BlockNode(Node):
    def __init__(self):
        super().__init__("block")
    
    def evaluate(self, symbol_table):
        for statement in self.children:
            if statement is not None:
                return_value = statement.evaluate(symbol_table)

        if self.value != 'Root':
            return return_value

class ConditionNode(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        if self.value == "kazo_nao":
            self.children[0].evaluate(symbol_table)
        elif self.children[0].evaluate(symbol_table)():
            self.children[1].evaluate(symbol_table)
        elif len (self.children) > 2:
            self.children[2].evaluate(symbol_table)

class FunctionDeclarationNode(Node):
    def __init__(self, value, type=None):
        super().__init__(value)
        self.type = type

    def evaluate(self, symbol_table):
        function_table.create(self.value, Function(self.type, self))

class FunctionCallNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):

        function = function_table.lookup(self.value)

        if self.children == [None]:
            self.children = []

        if len(self.children) != len(function.reference.children[1:-1]):
            raise Exception(
                f'Incorrekt number of argumentz: expekted {len(function.reference.children[1:])} got {len(self.children)}')

        function_symbol_table = SymbolTable()

        for passed_arg, expected_arg in zip(self.children, function.reference.children[1:-1]):

            if passed_arg.evaluate(symbol_table).operand_data_type != expected_arg.operand_data_type:
                raise Exception(f'Incorrekt type of argument {passed_arg.value}: expekted {expected_arg.operand_data_type} and got {passed_arg.evaluate().operand_data_type}')
            
            expected_arg.evaluate(function_symbol_table)
            function_symbol_table.assign(expected_arg.children[0].value, passed_arg.evaluate(symbol_table))

        return function.reference.children[-1].evaluate(function_symbol_table)

class IdentifierNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        variable_name = self.value
        return symbol_table.lookup(variable_name)

class IntVal(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return Variable(self.value, int)

class NoOp(Node):
    def __init__(self):
        super().__init__("[NULL]")

    def evaluate(self, symbol_table):
        pass

class PrintNode(Node):
    def __init__(self):
        super().__init__("komunikar")

    def evaluate(self, symbol_table):
        if self.children[0].evaluate(symbol_table) is not None:
            expr_value = self.children[0].evaluate(symbol_table)()
            print(expr_value)
        else:
          #  print(1)
            pass

class ReadNode(Node):
    def __init__(self):
        super().__init__("kaptar")

    def evaluate(self, symbol_table):
        expr_value = int(input(''))
        return Variable(expr_value, int)

class ReturnNode(Node):
    def __init__(self):
        super().__init__('entregue')

    def evaluate(self, symbol_table):
        return self.children[0].evaluate(symbol_table)

class StringNode(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, symbol_table):
        return Variable(self.value, str)
        
class UnOp(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, symbol_table):
        child_value = self.children[0].evaluate(symbol_table)
        if self.value == '-':
            return -child_value
        elif self.value == '+':
            return child_value
        elif self.value == '!':
            return child_value.__not__()
        else:
            raise SyntaxError("erro on unary operator")

class VarDecNode(Node):
    def __init__(self, operand_data_type=None):
        super().__init__('VarDec')
        self.operand_data_type = operand_data_type

    def evaluate(self, symbol_table):
        for child in self.children:
            symbol_table.create(child.value, Variable(2 if self.operand_data_type == int else '', self.operand_data_type))
            
class WhileNode(Node):
    def __init__(self):
        super().__init__("enquanto")

    def evaluate(self, symbol_table):
        while self.children[0].evaluate(symbol_table)():
            self.children[1].evaluate(symbol_table)
        self.children[1].evaluate(symbol_table)





