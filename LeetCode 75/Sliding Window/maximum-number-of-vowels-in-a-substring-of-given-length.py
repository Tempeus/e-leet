class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(letter):
            return letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"

        max_match = 0
        first = 0
        next_value = k
        substr = s[:k]
        for c in substr:
            if is_vowel(c):
                max_match += 1
        
        cur_match = max_match
        while(len(s) > next_value):
            if is_vowel(s[first]):
                cur_match -= 1
            
            if is_vowel(s[next_value]):
                cur_match += 1
            
            if(cur_match > max_match):
                max_match = cur_match

            first += 1
            next_value += 1

        return max_match