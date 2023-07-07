class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        match_index = 0
        max_index = len(s)
        matches = 0
        for letter in t:
            if match_index < max_index and letter == s[match_index]:
                matches += 1
                match_index += 1
        return matches == max_index