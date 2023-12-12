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
        return self.x
    
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
        return self.left.calc() / self.right.calc()

def main():
    a = Num(345)
    b = Num(5)
    c = Num(1296)
    d = Num(216)
    #express = "345/5-(1296/216)"
    calculation1 = Minus(Div(a,b),Div(c,d))
    res = 345/5-(1296/216)
    print(calculation1.calc()==res)
main()

