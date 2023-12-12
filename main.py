
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):#first and last are of type Node: itself also has attribute next, and in addition it also has prev and val fields.
        self.first = None
        self.last = None
    def isEmpty(self):
        return self.first is None
    def push(self,val):
        if self.isEmpty():
            self.first = self.last = Node(val)
        else:
            newNode = Node(val)
            self.last.next = newNode
            newNode.prev = self.last
            self.last = newNode
    def pop(self):
        if(self.isEmpty()):
            return None
        x = self.last
        if x is self.first:
            self.first = self.last = None
        else:
            newLast = self.last.prev
            newLast.next = None
            self.last = newLast
        #x.prev = None
        return x.val
    def printStack(self):
        traverser = self.first
        while traverser is not None:
            print(traverser.val)
            traverser = traverser.next

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    def isEmpty(self):
        return self.first is None
    def enqueue(self,val):
        newNode = Node(val)
        if self.isEmpty():
            self.first = self.last = newNode
            return
        self.last.next = newNode
        newNode.prev = self.last
        self.last = newNode
    def dequeue(self):
        if self.isEmpty():
            return None
        popped = self.first.val
        if self.first is self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        return popped
    def printQueue(self):
        traverser = self.first
        while traverser is not None:
            print(traverser.val)
            traverser = traverser.next   

def parser(exp):
    S = Stack()
    Q = Queue()
    i = 0
    while i< len(exp):
        c = exp[i]
        print(f"i={i}, c={c}")
        if c.isnumeric():
            Q.enqueue(c)
        else:
            if c=="+" or c=="-":
                poppedOp = S.pop()  
                if poppedOp is not None and poppedOp == "*" or poppedOp == "/":
                    Q.enqueue(poppedOp)
                elif poppedOp is not None:
                    S.push(poppedOp)
                S.push(c)
            if c==")":
                #need to pop stacks 'til we get to a (
                stack_head = S.pop()
                while stack_head != None:
                    if stack_head =="(":
                        break
                    Q.enqueue(stack_head)
                    stack_head = S.pop()
            if c=="*" or c=="/":
                S.push(c)
        i=i+1
    #finished going over expression and making the Queue and the stack.
    #Now, to empty the rest of the stack to the queue
    while not S.isEmpty():
        x = S.pop()
        if x is not None:
            Q.enqueue(x)
    # print("Empying stack into queue...")
    # print("Stack is: ")
    # S.printStack()
    # print("Queue is: ")
    # Q.printQueue()
    #now, to put numbers in Stack
    while Q.first is not None:
        if Q.first.val.isnumeric():
            S.push(float(Q.first.val))
        else:
            y = S.pop()
            x = S.pop()
            op = Q.first.val
            print(f"op is {op}")
            if op=="/":
                S.push(x/y)
            elif op=="*":
                S.push(x*y)
            elif op=="-":
                S.push(x-y)
            elif op=="+":
                S.push(x+y)
        Q.dequeue()
            
    Q.printQueue()
    #emptied the first numbers in the queue to the stack
    print("Stack is: ")
    S.printStack()
    print("Queue is: ")
    Q.printQueue()
    return S.pop()

retval = parser("3-(5/2)")

print(f"expression is equal to: {retval}")
