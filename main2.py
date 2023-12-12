from DLL import Queue,Stack

def extract_whole_number(expression,start_index):
    i = start_index
    while expression[i].isnumeric():
        i+=1
    return i
def main2():
    Q = Queue()
    S = Stack()
    expression = "(12345+1+65+98+999+10000+1+6)"
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
        else:
            char = expression[i]
            print(char)
            if char == "(" or char == "/" or char =="*":
                S.push(char)
            elif char == "-" or char == "+":
                #NEED TO CONSERVE ORDER OF OPERATIONS: All DIV AND MUL OPS MUST COME BEFORE PLUS AND MINUS OPS
                p = S.last
                while not S.is_empty() and (p=="*" or p=="/"):
                    Q.enqueue(S.pop())
                S.push(char)
            elif char == ")":#need to pop all stack items into the queue,until we reach an (
                p = S.last
                while S.last!="(":
                    Q.enqueue(S.pop())
            i+=1
    #Now, to dump what operations may remain in the Stack into the Queue

    while not S.is_empty():
        Q.enqueue(S.pop())

    #--------FINISHED going over input expression and preparing the output queue--------------
    

main2()