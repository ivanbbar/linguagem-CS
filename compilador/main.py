import sys
from parser import Parser
from tablesx import symbol_table

if __name__ == "__main__":
    
    input_str = "./scripts/test1.antic"
    
    with open(input_str, 'r') as f:
        input_expr = f.read()
    
    root = Parser.interpret(input_expr)    
    root.evaluate(symbol_table)