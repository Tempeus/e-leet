def mergeAlternately(word1: str, word2: str) -> str:
    w1len = len(word1)
    w2len = len(word2)
    w1 = list(word1.strip())
    w2 = list(word2.strip())

    ret = ""
    w1idx = 0
    w2idx = 0
    for i in range(w1len + w2len):
        if w1idx >= w1len:
            for char in w2[w2idx:]:
                ret += char
            return ret
        elif w2idx >= w2len:
            for char in w1[w1idx:]:
                ret += char
            return ret
        elif w1idx <= w2idx:
            ret += (w1[w1idx])
            w1idx += 1 
        elif w1idx > w2idx:
            ret += (w2[w2idx])
            w2idx += 1
    return ret