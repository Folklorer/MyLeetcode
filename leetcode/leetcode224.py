# 240729

def calculate(s: str) -> int:
    stack = []
    num = 0
    pos = 1
    ans = 0
    for c in s:
        if c == ' ':continue
        if c not in [' ','+','-','(',')']:
            num = 10*num + int(c)
        elif c == '+' or c == '-':
            ans += pos * num
            num = 0
            pos = 1 if c=='+' else -1
        elif c == '(':
            stack.append((ans,pos))
            ans = 0
            pos = 1
        elif c == ')':
            ans += pos * num
            num = 0
            a, b = stack.pop()
            ans = a + b * ans
        print(stack,ans,num,pos)
    return ans+num*pos


s = "1 + 1"
print(calculate(s))

