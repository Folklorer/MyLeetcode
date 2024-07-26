# 240725
# totally similar to leetcode 205

def wordPattern(pattern: str, s: str):
    s = s.split(' ')
    if len(s) != len(pattern):return False
    hash1, hash2 = {}, {}
    for i in range(len(pattern)):
        if (pattern[i] in hash1 and hash1[pattern[i]]!=s[i]) or (s[i] in hash2 and hash2[s[i]]!=pattern[i]):
            return False
        hash1[pattern[i]] = s[i]
        hash2[s[i]] = pattern[i]
    return True

a = "abbc"
b = "apple bee dog cat"
print(wordPattern(a,b))
