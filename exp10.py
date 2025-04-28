stack = []

def push(element):
    stack.append(element)
    print(f"{element} pushed into stack")
def pop():
    if len(stack)==0:
        print("stack is empty. cannot pop.")
    else :
        popp_e=stack.pop()
        print(f"{popp_e} poped from the stack.")
def display():
    if len(stack) == 0:
        print("stack is empty")
    else : 
        print("current Stack:",stack)
push(10)
push(20)
push(30)

display()
pop()
display()
