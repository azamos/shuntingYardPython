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
        if self.right.calc() == 0:
            raise ValueError("Division by zero")
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
            Q.append(Num(parsed_num))
            i=lsd
        else:
            char = expression[i]
            if char == "(" or char == "/" or char =="*":
                S.append(char)
            elif char == "-" or char == "+":
                #first, a check to differentiate between the operator Minus (a-b) vs the sign (-5)
                if char =="-" and S[-1]=="(" and i+1<len(expression) and expression[i+1].isnumeric():
                    least_significant_bit = extract_whole_number(expression,i+1)
                    neg_num_string = expression[i:least_significant_bit]
                    parsed_neg_num = float(neg_num_string)
                    Q.append(Num(parsed_neg_num))
                    i=least_significant_bit
                    continue
                else:
                    #NEED TO CONSERVE ORDER OF OPERATIONS: All DIV AND MUL OPS MUST COME BEFORE PLUS AND MINUS OPS
                    while S and (S[-1]=="*" or S[-1]=="/"):
                        Q.append(S.pop())
                    S.append(char)
            elif char == ")":#need to pop all stack items into the queue,until we reach an (
                while S:
                    stack_top = S.pop()
                    if stack_top == "(":
                        break
                    else:
                        Q.append(stack_top)
            i+=1

    #Now, to dump what operations may remain in the Stack into the Queue

    while S:#NOTE: this could be the source of the problem,
            #since here we just dump whatever leftover operators are in the stack
        Q.append(S.pop())

    #--------FINISHED going over input expression and preparing the output queue--------------

    #Now, I must dequeue all the numbers into the stack until meeting an op, perform that op on the stack head
    #and its predecessor, pop `em, and append the result of the op into the stack, ad infinitum
    while Q:
        element = Q.pop(0)
        if isinstance(element,Num):
            S.append(element)
        else:
            op1 = S.pop()
            op2 = S.pop()
            res = 0
            if element == "/":
                res = Div(op1,op2)
            elif element == "*":
                res = Mul(op1,op2)
            elif element == "-":
                res = Minus(op1,op2)
            elif element == "+":
                res = Plus(op1,op2)
            S.append(Num(res.calc()))

    return S.pop().calc()

def extract_whole_number(expression,start_index):
    i = start_index
    while i<len(expression) and expression[i].isnumeric() or expression[i]==".":#needed i<len(expression), otherwise error when the last
                                                          #characters form a number
        i+=1

    return i

expression = "(27-(-66)+39)"
res = parser(expression)
exp = eval(expression)
print(f"res={res},exp={exp}, they are { 'not' if res!=exp else ''} equal")
