# 240729

def evalRPN(tokens: list[str]) -> int:
    stack = []
    for word in tokens:
        print(stack)
        if word not in ['+','-','*','/']:
            word = int(word)
            stack.append(word)
            continue
        if word == '+':
            stack.append(stack.pop()+stack.pop())
        elif word == '-':
            stack.append(-stack.pop()+stack.pop())
        elif word == '*':
            stack.append(stack.pop()*stack.pop())
        elif word == '/':
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            
            stack.append(tmp2//tmp1 + int(tmp2//tmp1 < 0 and tmp2%tmp1!=0))
    return stack.pop()

tokens = ["4","-2","/","2","-3","-","-"]
print(evalRPN(tokens))