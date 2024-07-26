# 240725

# RunTime ERROR: pass 111/126
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    ans = []
    def is_posdifword(s,t):
        return sorted(s) == sorted(t)
    while strs:
        tmp = [strs[0]]
        idx = [0]
        flag = strs[0]
        for i, word in enumerate(strs):
            if i==0: continue
            if is_posdifword(flag,word):
                tmp.append(word)
                idx.append(i)
        for i in reversed(idx):
            del strs[i]
        ans.append(tmp)
    return ans

# hash table hint: FIND THE CONFLICT!!!
def groupAnagrams2(strs: list[str]) -> list[list[str]]:
    mydict = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in mydict:
            mydict[sorted_word] = [word]
        else:
            mydict[sorted_word].append(word)
    ans = []
    for value in mydict.values():
        ans.append(value)
    return ans


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams2(strs))
