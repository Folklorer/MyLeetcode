# 240730
def myPow(x: float, n: int) -> float:
    if n == 1 : return x
    elif n == 0 : return 1
    elif n == -1: return 1/x
    return myPow(x,n//2) ** 2 if n % 2 == 0 else myPow(x,n//2) ** 2 * x


def getGoodIndices(variables: list[list[int]], target: int) -> list[int]:
    if not variables:
        return []
    if not variables[0]:
        return []
    ans = []
    for i in range(len(variables)):
        if pow(pow(variables[i][0],variables[i][1], 10) , variables[i][2], variables[i][3]) == target:
            ans.append(i)
    return ans

# actually pow(x,y,z) == x**y %z

variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
target = 2
print(getGoodIndices(variables,target))