class DLL_Node:
    def __init__(self,val) -> None:
        self.val=val
        self.next = None
        self.prev = None
class DLL:
    def __init__(self) -> None:
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None
    
    def insert(self,new_val):
        new_node = DLL_Node(new_val)
        if self.is_empty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
    
    #this is the only relevant method in relation to FIFO or LIFO
    def delete(self,fifo=True):
        #empty, return None to imply empty stack
        if self.is_empty():
            return None
        #if length is 1, does not matter if FIFO or LIFO, acts the exact same way
        if self.first is self.last:
            val = self.first.val
            self.first = self.last = None
            return val
        
        if fifo:#e.g a Queue
            old_head = self.first#first in is the first out
            new_head = self.first.next#next in line to be out, is the next after it
            #discconecting the old head from the new head
            new_head.prev = None
            old_head.next = None
            #setting the new head of the Queue
            self.first = new_head
            return old_head.val
        
        else:#lifo, e.g a Stack
            old_head = self.last#last in is the first out
            new_head = old_head.prev#next is his predecessor
            #disconnecting new head from old head
            old_head.prev = None
            new_head.next = None
            #setting the new head of the stack
            self.last = new_head
            return old_head.val

class Stack(DLL):
    def __init__(self) -> None:
        super().__init__()
    def push(self,new_val):
        self.insert(new_val)
    def pop(self):
        return self.delete(fifo=False)
    def printStack(self):
        #Print From last to first
        p = self.last
        i = 1
        print(f"Stack head is {self.last.val}, the newest element inn the Stack\n")
        while p is not None:
            print(f"item #{i}: {p.val}")
            i += 1
            p = p.prev
        print(f"Last item in the Stack is  {self.first.val}\n")

class Queue(DLL):
    def __init__(self) -> None:
        super().__init__()
    def enqueue(self,new_val):
        self.insert(new_val)
    def dequeue(self):
        return self.delete(fifo=True)
    def printQueue(self):
        #Print From first to last
        p = self.first
        i = 1
        print(f"Queue head is {self.first.val},the oldest element in the queue\n")
        while p is not None:
            print(f"item #{i}: {p.val}")
            i += 1
            p = p.next
        print(f"\nLast item in the Queue is  {self.last.val}\n")
    
# S = Stack()
# Q = Queue()
# for i in range(1,10):
#     S.push(i**2)
#     Q.enqueue((2*i)**2)
# print("Printing the stack, S: ")
# S.printStack()
# print("Printing the queue, Q: ")
# Q.printQueue()   

# ###################
# #popping top of the stack, and dequeing the queue
# print(f"Popped stack: {S.pop()}")
# print(f"Dequeued queue: {Q.dequeue()}")
# print("-----------------AFTER POPPING AND DEQUEUEING---------------------")
# print("Printing the stack, S: ")
# S.printStack()
# print("Printing the queue, Q: ")
# Q.printQueue()   


            
