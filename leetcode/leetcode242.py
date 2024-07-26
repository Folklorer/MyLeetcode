# 240725
from collections import Counter

# Similar to leetcode 383 but inefficient 
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    mydict = Counter(s)
    for i in range(len(t)):
        if not t[i] in mydict:
            return False
        mydict[t[i]] -= 1
        if mydict[t[i]] < 0:
            return False
    for value in mydict.values():
        if value != 0:
            return False
    return True 

def isAnagram2(s: str, t: str) -> bool:
    return sorted(s)==sorted(t)
