class Function:
    def __init__(self, type, reference):
        self.type = type
        self.reference = reference

class List(list):
    def __init__(self, __owner):
        super(List, self).__init__()
        self.__owner = __owner

    def append(self, __object) -> None:
        super(List, self).append(__object)

class Variable:
    def __init__(self, value, operand_data_type):
        if isinstance(value, bool):
            value = int(value)
        self.value = value
        self.operand_data_type = operand_data_type

    def __call__(self):
        return self.operand_data_type(self.value)

    def __add__(self, other):
        if isinstance(other, Variable) and isinstance(self.value, int) and isinstance(other.value, int):
            return Variable(self.value + other.value, self.operand_data_type)
        elif isinstance(other, int) and isinstance(self.value, int):
            return Variable(self.value + other, self.operand_data_type)
        else:
            raise Exception(f'Unsupported operation + between {self.operand_data_type} and {other.operand_data_type}')

    def __sub__(self, other):
        if isinstance(other, Variable) and isinstance(self.value, int) and isinstance(other.value, int):
            return Variable(self.value - other.value, self.operand_data_type)
        elif isinstance(other, int) and isinstance(self.value, int):
            return Variable(self.value - other, self.operand_data_type)
        else:
            raise Exception(f'Unsupported operation - between {self.operand_data_type} and {other.operand_data_type}')

    def __mul__(self, other):
        if isinstance(other, Variable) and isinstance(self.value, int) and isinstance(other.value, int):
            return Variable(self.value * other.value, self.operand_data_type)
        elif isinstance(other, int) and isinstance(self.value, int):
            return Variable(self.value * other, self.operand_data_type)
        else:
            raise Exception(f'Unsupported operation * between {self.operand_data_type} and {other.operand_data_type}')

    def __floordiv__(self, other):
        if isinstance(other, Variable) and isinstance(self.value, int) and isinstance(other.value, int):
            return Variable(self.value // other.value, self.operand_data_type)
        elif isinstance(other, int) and isinstance(self.value, int):
            return Variable(self.value // other, self.operand_data_type)
        else:
            raise Exception(f'Unsupported operation // between {self.operand_data_type} and {other.operand_data_type}')

    def __and__(self, other):
        return Variable(self() and other(), self.operand_data_type)

    def __or__(self, other):
        return Variable(self() or other(), self.operand_data_type)

    def __eq__(self, other):
        return Variable(self() == other(), self.operand_data_type)

    def __lt__(self, other):
        return Variable(self() < other(), self.operand_data_type)

    def __gt__(self, other):
        return Variable(self() > other(), self.operand_data_type)

    def __concat__(self, other):
        return Variable(str(self.value) + str(other.value), str)

    def __pos__(self):
        return self

    def __neg__(self):
        return Variable(-self(), self.operand_data_type)

    def __not__(self):
        return Variable(not self.value, self.operand_data_type)