from typing import List


def missingNumber(nums: List[int]) -> int:
    nums = set(nums)

    for i in range(1,len(nums)+1):
        if i not in nums:
            return i
        else:
            i += 1
    return 0