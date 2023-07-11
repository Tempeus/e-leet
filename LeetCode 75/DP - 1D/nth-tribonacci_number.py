class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            tn = 0
            tn1 = 1
            tn2 = 1
            tn3 = 0
            for i in range(n-2):
                tn3 = tn + tn1 + tn2
                tn = tn1
                tn1 = tn2
                tn2 = tn3
            return tn3