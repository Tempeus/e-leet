class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        left = 0
        right = len(s) - 1
        left_b = False
        right_b = False
        s = list(s)
        while(left < right):
            if not left_b:
                if s[left] not in vowel:
                    left += 1
                else:
                    left_b = True
            if not right_b:
                if s[right] not in vowel:
                    right -= 1
                else:
                    right_b = True
            if right_b and left_b:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
                left_b = False
                right_b = False
        
        return "".join(s)