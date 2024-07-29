# 240726

# 可以直接用列表代替stack
def isValid(s: str) -> bool:
    class Stack:
        def __init__(self):
            self.items = []
        def is_empty(self):
            return len(self.items) == 0
        def push(self, item):
            self.items.append(item) 
        def pop(self):
            if not self.is_empty():
                return self.items.pop() 
    stack = Stack()
    dic = {")":"(", "}":"{", "]":"["}
    if not s: return False
    if s[0] in dic: return False
    for c in s:
        if c not in dic:
            stack.push(c)
        else:
            if stack.pop() != dic[c]:
                return False
    return stack.is_empty()

s = "()[]{}"
print(isValid(s))