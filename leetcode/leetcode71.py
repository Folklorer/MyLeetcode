# 240729

def simplifyPath(path: str) -> str:
    lst = path.split('/')
    stack = []
    for i in lst:
        if i not in ['','.','..']:
            stack.append(i)
        elif i == '..':
            stack.pop(-1)
    return '/'+'/'.join(stack)

path = "/.../a/../b/c/../d/./"
print(simplifyPath(path))