
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
from tokens import EndToken
from tokens import AssignmentToken
from tokens import IdentifierToken
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

from datax import Variable, List, Function

from tokenizer import PrePro, Tokenizer

from nodes import Node
from nodes import BinOp
from nodes import IntVal
from nodes import UnOp
from nodes import NoOp
from nodes import IdentifierNode
from nodes import AssignNode
from nodes import PrintNode
from nodes import ReadNode
from nodes import BlockNode
from nodes import ConditionNode
from nodes import WhileNode
from nodes import StringNode
from nodes import VarDecNode
from nodes import FunctionDeclarationNode
from nodes import FunctionCallNode
from nodes import ReturnNode

def instance_possible(token):
    return isinstance(token, (NumericToken, PlusToken, MinusToken, LeftParenToken, RightParenToken, IdentifierToken, NotToken, ReadToken, EqualToken, StringToken, DotToken))

instance_possible_relex = (IdentifierToken, NumericToken, PlusToken, MinusToken, LeftParenToken, NotToken, ReadToken, StringToken)

class Parser:
    tokenizer: Tokenizer = None

    @staticmethod
    def parse_rel_expression():
        Parser.tokenizer.select_next()
        if instance_possible(Parser.tokenizer.next):
            node = Parser.parse_expression()
            while isinstance(Parser.tokenizer.next, (EqualToken, GTToken, LTToken, DotToken)):
                if isinstance(Parser.tokenizer.next, EqualToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="==")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_expression())
                        node = node2 
                    else:
                        raise SyntaxError
                elif isinstance(Parser.tokenizer.next, GTToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value=">")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_expression())
                        node = node2 
                    else:
                        raise SyntaxError
                elif isinstance(Parser.tokenizer.next, LTToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="<")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_expression())
                        node = node2 
                    else:
                        raise SyntaxError
                elif isinstance(Parser.tokenizer.next, DotToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value=".")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_expression())
                        node = node2 
                    else:
                        raise SyntaxError
            return node
        raise SyntaxError("Error on parse_rel_expression")
            
    @staticmethod
    def parse_expression():
        # Parse an expression consisting of one or more terms separated by + or - operators        
        if instance_possible(Parser.tokenizer.next):            
            node = Parser.parse_term()
            while isinstance(Parser.tokenizer.next, (PlusToken, MinusToken, OrToken)):
                if isinstance(Parser.tokenizer.next, PlusToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="+")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_term())
                        node = node2 
                    else:
                        raise SyntaxError
                elif isinstance(Parser.tokenizer.next, MinusToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="-")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_term())
                        node = node2 
                    else:
                        raise SyntaxError
                elif isinstance(Parser.tokenizer.next, OrToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="||")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_term())
                        node = node2
            return node
        raise SyntaxError("Error on parse_expression")
            
    @staticmethod
    def parse_term():
        # Parse a term consisting of one or more factors separated by * or / operators
        if instance_possible(Parser.tokenizer.next):            
            node = Parser.parse_factor()
            while isinstance(Parser.tokenizer.next, (MultToken, DivToken, AndToken)):
                if isinstance(Parser.tokenizer.next, MultToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="*")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_factor())
                        node = node2 
                    else:
                        raise SyntaxError
                elif isinstance(Parser.tokenizer.next, DivToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="/")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_factor())
                        node = node2 
                    else:
                        raise SyntaxError
                elif isinstance(Parser.tokenizer.next, AndToken):
                    Parser.tokenizer.select_next()
                    if instance_possible(Parser.tokenizer.next):
                        node2 = BinOp(value="&&")
                        node2.children.append(node)
                        node2.children.append(Parser.parse_factor())
                        node = node2 
            
            return node
        raise SyntaxError("Error on parse_term")

    @staticmethod
    def parse_factor():
        # Parse a factor, which is either a number or an expression enclosed in parentheses
        node = None
        if isinstance(Parser.tokenizer.next, NumericToken):
            node = IntVal(Parser.tokenizer.next.value)
            Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, StringToken):
            node = StringNode(Parser.tokenizer.next.value)
            Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, PlusToken):
            node = UnOp('+')
            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_factor())
        elif isinstance(Parser.tokenizer.next, MinusToken):
            node = UnOp('-')
            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_factor())
        elif isinstance(Parser.tokenizer.next, NotToken):
            node = UnOp('!')
            Parser.tokenizer.select_next()
            node.children.append(Parser.parse_factor())
        elif isinstance(Parser.tokenizer.next, LeftParenToken):
            node = Parser.parse_rel_expression()
            if not isinstance(Parser.tokenizer.next, RightParenToken):
                raise SyntaxError('Unmatched left parenthesis')                
            Parser.tokenizer.select_next()
        elif isinstance(Parser.tokenizer.next, ReadToken):
            node = ReadNode()
            Parser.tokenizer.select_next()
            if isinstance(Parser.tokenizer.next, LeftParenToken):
                Parser.tokenizer.select_next()
                if not isinstance(Parser.tokenizer.next, RightParenToken):
                    raise SyntaxError('Unmatched left parenthesis')
            else:
                raise Exception("Missing left parenthesis")
            Parser.tokenizer.select_next()

        elif isinstance(Parser.tokenizer.next, IdentifierToken):
            if isinstance(Parser.tokenizer.check_next()[0], LeftParenToken):
                node = FunctionCallNode(Parser.tokenizer.next.value)
                Parser.tokenizer.select_next()

                while isinstance(Parser.tokenizer.next, (CommaToken,) + instance_possible_relex):
                    node.children.append(Parser.parse_rel_expression())
                    if not isinstance(Parser.tokenizer.next, (CommaToken, RightParenToken)):
                        raise Exception(f"Expected comma to separate arguments, received {Parser.tokenizer.next.value}")
                if not isinstance(Parser.tokenizer.next, RightParenToken):
                    raise Exception(f"Missing closing parenthesis, received {Parser.tokenizer.next.value}")
                Parser.tokenizer.select_next()
            else:
                node = IdentifierNode(Parser.tokenizer.next.value)
                Parser.tokenizer.select_next()

        return node
    
    @staticmethod
    def parse_statement():
        node = None

        if isinstance(Parser.tokenizer.next, (BreakToken, IdentifierToken, PrintToken, WhileToken, IfToken, VarDecToken)):

            if isinstance(Parser.tokenizer.next, BreakToken):
                node = NoOp()
                return node

            elif isinstance(Parser.tokenizer.next, IdentifierToken):
                if isinstance(Parser.tokenizer.check_next()[0], AssignmentToken):
                    var = IdentifierNode(Parser.tokenizer.next.value)
                    Parser.tokenizer.select_next()
                    statement = AssignNode()
                    statement.children.append(var)
                    statement.children.append(Parser.parse_rel_expression())
                    return statement
                elif isinstance(Parser.tokenizer.check_next()[0], VarDecToken):
                    var = IdentifierNode(Parser.tokenizer.next.value)
                    Parser.tokenizer.select_next()
                    
                    if not isinstance(Parser.tokenizer.check_next()[0], (TypeToken)):
                        raise SyntaxError(f"After declare a variable, you must use a type. Token found: {Parser.tokenizer.next.value}")

                    operand_data_type = None

                    if Parser.tokenizer.check_next()[0].value == "String":
                        operand_data_type = str
                    elif Parser.tokenizer.check_next()[0].value == "Int":
                        operand_data_type = int
                    
                    statement = VarDecNode(operand_data_type)
                    statement.children.append(var)
                    Parser.tokenizer.select_next()
                    
                    if isinstance(Parser.tokenizer.check_next()[0], AssignmentToken):
                        statement.children.append(Parser.parse_rel_expression())

                    return statement
                elif isinstance(Parser.tokenizer.check_next()[0], LeftParenToken):
                    statement = FunctionCallNode(Parser.tokenizer.next.value)
                    Parser.tokenizer.select_next()

                    while isinstance(Parser.tokenizer.next, (CommaToken,) + instance_possible_relex):
                        statement.children.append(Parser.parse_rel_expression())
                        Parser.tokenizer.select_next()
                        if not isinstance(Parser.tokenizer.next, (CommaToken, RightParenToken)):
                            raise Exception(f"Expected comma to separate arguments, received {Parser.tokenizer.next.value}")
                    if isinstance(Parser.tokenizer.next, RightParenToken):
                        Parser.tokenizer.select_next()

                    else:
                        raise Exception(f"Missing closing parenthesis, received {Parser.tokenizer.next.value}")

                    return statement
                else:
                    raise SyntaxError('Invalid assignment')
                
            elif isinstance(Parser.tokenizer.next, PrintToken):
                node = PrintNode()
                Parser.tokenizer.select_next()
                if isinstance(Parser.tokenizer.next, LeftParenToken):
                    expr = Parser.parse_rel_expression()
                    if isinstance(Parser.tokenizer.next, RightParenToken):
                        Parser.tokenizer.select_next()
                        node.children.append(expr)
                    else:
                        raise SyntaxError('Missing closing parenthesis')
                else:
                    raise SyntaxError('Missing opening parenthesis')

                if not isinstance(Parser.tokenizer.next, BreakToken):
                    raise SyntaxError('Missing break token')
            
            elif isinstance(Parser.tokenizer.next, WhileToken):
                node = WhileNode()
                node.children.append(Parser.parse_rel_expression())

                if not isinstance(Parser.tokenizer.next, BreakToken):
                    raise SyntaxError('Missing break token to open while')

                Parser.tokenizer.select_next()
                block = BlockNode()

                while isinstance(Parser.tokenizer.next, (IdentifierToken, PrintToken, WhileToken, IfToken, BreakToken, VarDecToken)):
                    block.children.append(Parser.parse_statement())
                    Parser.tokenizer.select_next()

                node.children.append(block)

                if not isinstance(Parser.tokenizer.next, EndToken):
                    raise SyntaxError('Missing end token to close while')
                
                Parser.tokenizer.select_next()
                if not isinstance(Parser.tokenizer.next, BreakToken):
                    raise SyntaxError('Missing break token to close while')

            elif isinstance(Parser.tokenizer.next, IfToken):
                node = ConditionNode("kazo")
                node.children.append(Parser.parse_rel_expression())

                if not isinstance(Parser.tokenizer.next, BreakToken):
                    raise SyntaxError('Missing break token')

                Parser.tokenizer.select_next()
                block = BlockNode()

                while isinstance(Parser.tokenizer.next, (IdentifierToken, PrintToken, WhileToken, IfToken, BreakToken)):
                    block.children.append(Parser.parse_statement())
                    Parser.tokenizer.select_next()
                
                node.children.append(block)

                if isinstance(Parser.tokenizer.next, ElseToken):
                    node_else = ConditionNode("kazo_nao")
                    Parser.tokenizer.select_next()
                    
                    if not isinstance(Parser.tokenizer.next, BreakToken):
                        raise SyntaxError('Missing break token on else')

                    Parser.tokenizer.select_next()
                    
                    while isinstance(Parser.tokenizer.next, (IdentifierToken, PrintToken, WhileToken, IfToken, BreakToken)):
                        node_else.children.append(Parser.parse_statement())
                        Parser.tokenizer.select_next()

                    node.children.append(node_else)

                if not isinstance(Parser.tokenizer.next, EndToken):
                    raise SyntaxError('Missing end token')

                Parser.tokenizer.select_next()  # Select next token after the EndToken

                if not isinstance(Parser.tokenizer.next, BreakToken):
                    raise SyntaxError('Missing break token to close if')
        
        elif isinstance(Parser.tokenizer.next, ReturnToken):
            node = ReturnNode()
            node.children.append(Parser.parse_rel_expression())

        elif isinstance(Parser.tokenizer.next, FunctionToken):
            Parser.tokenizer.select_next()
            if not isinstance(Parser.tokenizer.next, IdentifierToken):
                raise Exception(f"Invalid syntax, expected identifier of function, received {Parser.tokenizer.next.value}")

            node = FunctionDeclarationNode(Parser.tokenizer.next.value)
            node.children.append(IdentifierNode(Parser.tokenizer.next.value))

            Parser.tokenizer.select_next()
            if not isinstance(Parser.tokenizer.next, LeftParenToken):
                raise Exception(f"Invalid syntax, expected open parenthesis, received {Parser.tokenizer.next.value}")

            expect_identifier = False
            while not isinstance(Parser.tokenizer.next, RightParenToken):
                Parser.tokenizer.select_next()

                if isinstance(Parser.tokenizer.next, IdentifierToken):
                    expect_identifier = False
                    child = VarDecNode()

                    while isinstance(Parser.tokenizer.next, (CommaToken, IdentifierToken)):
                        if isinstance(Parser.tokenizer.next, CommaToken):
                            Parser.tokenizer.select_next()
                            next_expected_token = IdentifierToken
                        if isinstance(Parser.tokenizer.next, IdentifierToken):
                            next_expected_token = (CommaToken, VarDecToken)
                        child.children.append(IdentifierNode(Parser.tokenizer.next.value))
                        Parser.tokenizer.select_next()
                        if not isinstance(Parser.tokenizer.next, next_expected_token):
                            raise Exception(
                                f"Expected {next_expected_token().type} token, instead received {Parser.tokenizer.next.value}")

                    if isinstance(Parser.tokenizer.next, VarDecToken):
                        Parser.tokenizer.select_next()
                        if isinstance(Parser.tokenizer.next, TypeToken):
                            operand_data_type = None

                            if Parser.tokenizer.next.value == "String":
                                operand_data_type = str
                            elif Parser.tokenizer.next.value == "Int":
                                operand_data_type = int

                        else:
                            raise Exception(
                                f'Missing type declaration of variable(s) {", ".join([_child.value for _child in child.children])}')
                    else:
                        raise Exception(f"Missing colon token, received {Parser.tokenizer.next.value}")

                    child.operand_data_type = operand_data_type

                    Parser.tokenizer.select_next()
                    if isinstance(Parser.tokenizer.next, CommaToken):
                        expect_identifier = True

                    node.children.append(child)

                elif isinstance(Parser.tokenizer.next, VarDecToken):
                    raise Exception(
                        f"Missing close parenthesis at parse declaration, received {Parser.tokenizer.next.value}")

                elif isinstance(Parser.tokenizer.next, RightParenToken):
                    break

                else:
                    raise Exception(f"Invalid token, received {Parser.tokenizer.next.value}")

            if expect_identifier:
                raise Exception(f"Expected identifier after comma")

            Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, VarDecToken):
                raise SyntaxError('Missing :: token to declare function') 

            Parser.tokenizer.select_next()
            if not isinstance(Parser.tokenizer.next, TypeToken):
                raise Exception(f"Expected type declaration of function")

            node.type = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, BreakToken):
                raise SyntaxError('Missing break token after function declaration')

            body_function = BlockNode()
            Parser.tokenizer.select_next()
            while not isinstance(Parser.tokenizer.next, EndToken):
                statement = Parser.parse_statement()
                body_function.children.append(statement)
                Parser.tokenizer.select_next()

            if not isinstance(Parser.tokenizer.next, EndToken):
                raise SyntaxError('Missing end token to close function') 

            Parser.tokenizer.select_next()  # Select next token after the EndToken

            if not isinstance(Parser.tokenizer.next, BreakToken):
                raise SyntaxError('Missing break token to close function')

            node.children.append(body_function)

        else:
            raise SyntaxError("Erro no Parse Statement")
        return node

    @staticmethod
    def parse_block():
        block_node = BlockNode()
        while not isinstance(Parser.tokenizer.next, EOFToken):
            statement = Parser.parse_statement()
            block_node.children.append(statement)
            Parser.tokenizer.select_next()
        return block_node
    
    @staticmethod
    def interpret(input_str):
        preprocessed_input =  PrePro.preprocess(input_str)
        Parser.tokenizer = Tokenizer(source=preprocessed_input)
        Parser.tokenizer.select_next()
        
        root_node = Parser.parse_block()
        Parser.tokenizer.select_next()

        if not isinstance(Parser.tokenizer.next, EOFToken):
            raise SyntaxError("EOF not found")

        return root_node