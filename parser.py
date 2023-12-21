from abc import ABC
from numpy import double
from abc import ABC,abstractmethod

class Expression(ABC):
    @abstractmethod
    def calc(self)->double:
        pass

# implement the classes here
class Num(Expression):
    def __init__(self,x) -> None:
        super().__init__()
        self.x=x
    def calc(self)->double:
        return self.x

class BinExp(Expression):
    def __init__(self,left,right) -> None:
        super().__init__()
        self.left = left
        self.right = right

class Plus(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    
    def calc(self) -> double:
        return self.left.calc() + self.right.calc()

class Minus(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    
    def calc(self) -> double:
        return self.left.calc() - self.right.calc()
    
class Mul(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    
    def calc(self) -> double:
        return self.left.calc() * self.right.calc()

class Div(BinExp):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)
    
    def calc(self) -> double:
        y = self.right.calc()
        if y==0:
            return None
        return self.left.calc() / y


#implement the parser function here
def parser(expression)->double:
    queue = []
    stack = []
    i = 0
    n = len(expression)
    while i<n:
        c = expression[i]
        #first, I check if it is the begining of a substring representing a
        #negative number.
        #Negative numbers with absolute value x are represented as '(-x)'
        if c == "(" and expression[i+1] == '-':
            #need to extract the entire number, and push it to the end of the queue
            j = number_end(expression,i+2)
            queue.append(Num(double(expression[i+1:j])))
            i = j+1#since it is '(-x)', after the end of the number must come a ')'
            continue#extracted the negative number, gotta go extract the next token
        
        #if encountered a positive number, just extract it and append to the queue
        if c.isnumeric():
            j = number_end(expression,i)
            numstr = expression[i:j]
            #print(numstr)
            queue.append(Num(double(numstr)))
            i=j
            continue

        #not explicitly stated, but if we got here,
        #the ramining options are either an operator or a parenthesis.
        #Thus, must seperate to 2 cases: if parenthesis, or an operator:
        if c=="(":
            stack.append(c)
            i+=1
            continue
        if c==")":
            while stack[-1]!="(":
                queue.append(stack.pop())
            stack.pop()
            i+=1
            continue
        #if code reached here, it means expression[i] is not '(',')', a
        #number, or a negative number (-x).
        #thus, it must be an operator.
        #need to seperate to 2 cases: if stack is empty,
        # i just push into it.
        #otherwise, I must take into account 2 things, whilst
        #observing the stack head:
        # 1.order of operations
        # 2. left associativity of Div and Minus
        
        #if stack is empty, just push into it
        if not stack:
            stack.append(c)
            i+=1

        #need to also look at what is already in the stack
        else:
            #this check takes care of 2 things: both of the importance of doing
            #(9-5)+1 instead of 9-(5+1), and the left associativity of -:
            #10-1-2-3 must be ((10-1)-2)-3
            if c=="+" or c=="-":
                if stack[-1] == "-" or stack[-1]=="/" or stack[-1]=="*":
                    while stack and (stack[-1] == "-" or stack[-1]=="/" or stack[-1]=="*"):
                        queue.append(stack.pop())
            #this check seves a similar purpose as above, only this time
            #Div is in the shoes of Minus, and Mul in the shoes of Plus
            elif c=="*" or c=="/":
                if stack[-1] == "/":
                    while stack and stack[-1]=="/":
                        queue.append(stack.pop())
            #either way, append the op to the stack, and advance i
            stack.append(c)
            i+=1
    #DONE EXTRACTING TOKENS
    #print("DONE EXTRACTING TOKENS.Emptying stack onto the queue...")
    while stack:
        queue.append(stack.pop())
    #Now to perform the computations.
    #Until the queue is empty, I must follow these steps:
    # 1.empty queue by FIFO into the stack, until meeting an op
    # 2. perform stack[-2] op stack[-1], replacing them with the result
    # 3. continue scanning for numbers and ops until empty
    while queue:
        if isinstance(queue[0],Num):
            stack.append(queue.pop(0))
        else:#now we have a binary operator
            B = stack.pop()
            A = stack.pop()
            op = queue.pop(0)
            if op == "+":
                stack.append(Plus(A,B))
            elif op == "-":
                stack.append(Minus(A,B))
            elif op =="*":
                stack.append(Mul(A,B))
            else:
                stack.append(Div(A,B))
    res = stack.pop().calc()
    #print(f"calc result: {res}")
    return res

def number_end(e,startindex):
    encountered_dot = False
    end = startindex+1
    while end<len(e) and e[end].isnumeric() or (not encountered_dot and e[end]=="."):
        if e[end]==".":
            encountered_dot = True
        end+=1
    return end

#parser("(-3)+17*5-(12/4*2)")