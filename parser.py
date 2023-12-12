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
        return self.left.calc() / self.right.calc()

#implement the parser function here
def parser(expression)->double:
    Q = []#a queue, only difference to a stack is to dequeue, must use Q.pop(0)
    S = []#a stack
    i=0
    #NOTE to self: there are multiple iterations occouring:
    #               1.The external one,for the input expression, going over characters one by one
    #               1.1. if we detect a digit, there is another, parallel check over the expression, to see
    #                    where the number ends(multiple digits number)
    #               2.if the char is - or +, we need to pop all * and / in the stack into the queue
    #                 until we reach the first -,+ or (.
    #               3.if the char is ), we need to pop all the ops in the stack, until we find a (.
    while i<len(expression):
        if expression[i].isnumeric():   
            lsd = extract_whole_number(expression,i)
            num_string = expression[i:lsd]

            parsed_num = float(num_string)
            Q.push(Num(parsed_num))
            i=lsd
        else:
            char = expression[i]
            #print(char)
            if char == "(" or char == "/" or char =="*":
                S.push(char)
            elif char == "-" or char == "+":
                #NEED TO CONSERVE ORDER OF OPERATIONS: All DIV AND MUL OPS MUST COME BEFORE PLUS AND MINUS OPS
                while S:
                    stack_top = S.pop()
                    if stack_top == "/" or stack_top == "*":
                        Q.push(stack_top)
                    else:
                        break
                S.push(char)
            elif char == ")":#need to pop all stack items into the queue,until we reach an (
                while S:
                    stack_top = S.pop()
                    if stack_top == "(":
                        break
                    else:
                        Q.push(stack_top)
            i+=1

    #Now, to dump what operations may remain in the Stack into the Queue

    while S:
        Q.push(S.pop())

    #--------FINISHED going over input expression and preparing the output queue--------------

    #Now, I must dequeue all the numbers into the stack until meeting an op, perform that op on the stack head
    #and its predecessor, pop `em, and push the result of the op into the stack
    while Q:
        element = Q.pop(0)
        if element.isnumeric():
            S.push(Num(float(element)))
        else:
            op2 = S.pop()
            op1 = S.pop()
            res = 0
            if element == "/":
                res = Div(op1,op2)
            elif element == "*":
                res = Mul(op1,op2)
            elif element == "-":
                res = Minus(op1,op2)
            elif element == "+":
                res = Plus(op1,op2)
            S.push(res.calc())

    return S.pop()

def extract_whole_number(expression,start_index):
    i = start_index
    while i<len(expression) and expression[i].isnumeric():#needed i<len(expression), otherwise error when the last
                                                          #characters form a number
        i+=1

    return i