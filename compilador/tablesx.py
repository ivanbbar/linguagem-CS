class FunctionTable:
    def __init__(self):
        self._symbols = {}

    def lookup(self, key):
        if key in self._symbols.keys():
            return self._symbols[key]
        raise SyntaxError(f"Undefined key for function '{key}'")

    def create(self, key, value):
        if key in self._symbols:
            raise ValueError(f"{key} variable already exists in current scope")
        self._symbols[key] = value

class SymbolTable:
    def __init__(self):
        self._symbols = {}

    def lookup(self, key):
        if key in self._symbols.keys():
            return self._symbols[key]
        raise SyntaxError(f"Undefined key '{key}'")

    def assign(self, key, value):
        if key not in self._symbols:
            raise ValueError(f"{key} variable not found in symbol table")
        if self._symbols[key].operand_data_type != value.operand_data_type:
            raise TypeError(f"Expected {self._symbols[key].operand_data_type}, got {value.operand_data_type}")
        self._symbols[key] = value

    def create(self, key, value):
        if key in self._symbols:
            raise ValueError(f"{key} variable already exists in current scope")
        self._symbols[key] = value

symbol_table = SymbolTable()
function_table = FunctionTable()