from abc import ABC
from numpy import double
from abc import ABC,abstractmethod

class Expression(ABC):
    @abstractmethod
    def calc(self)->double:
        pass

# implement the classes here
class Num(ABC):
    def __init__(self,x) -> None:
        super().__init__()
        self.x = x
    def calc(self)->double:
        return double(x)
    
class BinExp(ABC):
    def __init__(self,left,right) -> None:
        super().__init__()
        self.left = left
        self.right = right

class Plus(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    def calc(self):
        return self.left.calc() + self.right.calc()

class Minus(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    def calc(self):
        return self.left.calc() - self.right.calc()

class Mul(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    def calc(self):
        return self.left.calc() * self.right.calc()
    
class Div(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    def calc(self):
        x = self.left.calc()
        y = self.left.calc()
        if y != 0:
            return x / y
        elif x == 0:
            return float('nan')
        else:
            sign = 1 if x > 0 else -1
            return sign*inf

#implement the parser function here
def parser(expression)->double:
    return 0.0

