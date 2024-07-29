# 240729

def calculate(s: str) -> int:
    stack = []
    flag = False
    for c in s:
        if c == ' ': continue
        if c not in ['(',')','+','-']:
            tmp = int(c)
            if stack and stack[-1] not in ['(',')','+','-']:
                stack.append(stack.pop()*10+tmp)
            else :
                stack.append(tmp)
        else: 
            if c in ['(','+','-']:
                stack.append(c)
            elif c == ')':
                tmp = stack.pop()
                while tmp != '(':
                    print(stack)
                    tp = stack.pop()
                    if tp == '+':
                        stack.append(tmp+stack.pop())
                        print(stack)
                    elif tp == '-':
                        if stack[-1] == '(':
                            stack.append(-tmp)
                        else:
                            stack.append(stack.pop()-tmp)
                    elif tp == '(':
                        stack.append(tmp)
                        break
                    tmp = stack.pop()
    ans = 0
    flag = True
    for i in stack:
        if i == '+':
            flag = True
        elif i == '-':
            flag = False
        else:
            if flag: ans+=i
            else: ans-=i
    return ans

s = "2-4-(8+2-6+(8+4-(1)+8-10))"
print(calculate(s))

