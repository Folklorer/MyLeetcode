# 240730

def myPow(x: float, n: int) -> float:
    if n == 1 : return x
    elif n == 0 : return 1
    elif n == -1: return 1/x
    return myPow(x,n//2) ** 2 if n % 2 == 0 else myPow(x,n//2) ** 2 * x


print(myPow(2,-2)) 