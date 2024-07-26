# 240725

from collections import Counter

def canConstruct(ransomNote: str, magazine: str):
    l1, l2 = len(ransomNote), len(magazine)
    if l2 < l1:
        return False
    dic1 = dict()
    dic2 = dict()
    for i in range(l2):
        if i<l1:
            if not magazine[i] in dic1:
                dic1[magazine[i]] = 1
            else:
                dic1[magazine[i]] += 1
            if not ransomNote[i] in dic2:
                dic2[ransomNote[i]] = 1
            else:
                dic2[ransomNote[i]] += 1
        else:
            if not magazine[i] in dic1:
                dic1[magazine[i]] = 1
            else:
                dic1[magazine[i]] += 1
    for key in dic2:
        if not key in dic1:
            return False
        elif dic2[key] > dic1[key]:
            return False
    return True

def canConstruct2(ransomNote: str, magazine: str):
    mydict = {chr(i): 0 for i in range(97, 97 + 26)}
    l1, l2 = len(ransomNote), len(magazine)
    if l2 < l1:
        return False
    else:
        for i in range(l2):
            if i<l1:
                mydict[magazine[i]] += 1
                mydict[ransomNote[i]] -= 1
            else:
                mydict[magazine[i]] += 1
    for value in mydict.values():
        if value < 0:
            return False
    return True

def canConstruct3(ransomNote: str, magazine: str):
    mydict = Counter(magazine)
    l1, l2 = len(ransomNote), len(magazine)
    if l2 < l1:
        return False
    for i in range(l1):
        if not ransomNote[i] in mydict:
            return False
        else:
            mydict[ransomNote[i]] -= 1
            if mydict[ransomNote[i]] < 0:
                return False
    return True



a = "aabbcc"
b = "aaabbc"
c = "aabbccdd"
print(canConstruct3(a,b))
print(canConstruct3(a,c))

