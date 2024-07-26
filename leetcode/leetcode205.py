# 240725

# poor method
def isIsomorphic(s: str, t: str):
    arr = [s.index(s[i]) == t.index(t[i]) for i in range(len(s))]
    return all(arr)

# a little little improvement: less storage
def isIsomorphic1(s: str, t: str):
    for i in range(len(s)):
        if not s.index(s[i]) == t.index(t[i]):
            return False
    return True

# poor time usage
def isIsomorphic2(s: str, t: str):
    hash1, hash2 = {}, {}
    for i in range(len(s)):
        if (s[i] in hash1 and hash1[s[i]]!=t[i]) or (t[i] in hash2 and hash2[t[i]]!=s[i]):
            return False
        hash1[s[i]] = t[i]
        hash2[t[i]] = s[i]
    return True

s = "badc"
t = "baba"
print(isIsomorphic2(s,t))
