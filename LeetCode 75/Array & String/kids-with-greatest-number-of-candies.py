class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        biggest = max(candies)
        for kid in candies:
            result.append(True if kid + extraCandies >= biggest else False)
        return result