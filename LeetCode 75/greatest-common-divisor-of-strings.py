from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #First check if it is divisible
        if(str1 + str2 == str2 + str1):
            #Find the greatest common divisor between the two lengths
            return str1[:gcd(len(str1), len(str2))]
        else:
            return ""