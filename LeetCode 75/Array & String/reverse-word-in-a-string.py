class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        print(s)
        ret = ""
        s.reverse()
        for t in s:
            if t != " " and t != "":
                ret += t + " "
        return ret[:len(ret) - 1]