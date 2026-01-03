def longestCommonPrefix(strs):
    res = ""
    # prefix = True
    for ch in zip(*strs):
        if len(set(ch)) == 1:
            res += ch[0]
        else:
            break

    return res

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))