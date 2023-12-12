from DLL import Queue,Stack

def extract_whole_number(expression,start_index):
    i = start_index
    while i<len(expression) and expression[i].isnumeric():#needed i<len(expression), otherwise error when the last
                                                          #characters form a number
        i+=1

    return i
def main2():
    Q = Queue()
    S = Stack()
    expression = "1+(23*333*81123759+51235*((37-1)/2))-3"
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
            print(num_string)
            Q.enqueue(num_string)#maybe just enqueue the number itself?
            #parsed_num = float(num_string)
            i=lsd
            if i==len(expression):
                print("\nWTF2\n")
                break
        else:
            # char = expression[i]
            # print(char)
            # if char == "(" or char == "/" or char =="*":
            #     S.push(char)
            # elif char == "-" or char == "+":
            #     #NEED TO CONSERVE ORDER OF OPERATIONS: All DIV AND MUL OPS MUST COME BEFORE PLUS AND MINUS OPS
            #     p = S.last
            #     while not S.is_empty() and (p=="*" or p=="/"):
            #         Q.enqueue(S.pop())
            #     S.push(char)
            # elif char == ")":#need to pop all stack items into the queue,until we reach an (
            #     p = S.last
            #     while S.last!="(":
            #         Q.enqueue(S.pop())
            i+=1
    print("prepared Stack and Queue:\n")
    Q.printQueue()
    S.printStack()
    #Now, to dump what operations may remain in the Stack into the Queue

    while not S.is_empty():
        Q.enqueue(S.pop())

    #--------FINISHED going over input expression and preparing the output queue--------------
    print("popped rest of Stack into the Queue:\n")
    Q.printQueue()
    S.printStack()
    #Now, I must dequeue all the numbers into the stack until meeting an op, perform that op on the stack head
    #and its predecessor, pop `em, and push the result of the op into the stack
    # while not Q.is_empty():
    #     element = Q.dequeue()
    #     if element.isnumeric():
    #         S.push(float(element))
    #     else:
    #         op2 = S.pop()
    #         op1 = S.pop()
    #         res = 0
    #         if element == "/":
    #             res = op1/op2
    #         elif element == "*":
    #             res = op1*op2
    #         elif element == "-":
    #             res = op1-op2
    #         elif element == "+":
    #             res = op1+op2
    #         S.push(res)
    # print("After evaluating the expression. Queue SHOULD BE EMPTY, and S should have on element, the eval result:\n")
    # Q.printQueue()
    # S.printStack()

main2()