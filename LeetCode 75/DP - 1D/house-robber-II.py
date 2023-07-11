class Solution:
    '''
    The idea is similar to how to solve house robber 1. 
    The only issue is the added constraint that [0] and [N] are adjacent to each other.
    This constraint means that if you choose the first index, you can't choose the last index.
    As a result, if we split the list into two sublists, each either containing [0] or [N]
    Example: [1,2,3,1] --> [1,2,3] or [2,3,1]

    With these two lists, we will apply the house robber 1 solution to each of them and we'll find the max of either lists to give us the answer.
    '''
    def rob(self, nums: List[int]) -> int:
        N = len(nums) - 1
        if N <= 2:
            return max(nums)

        nums1 = nums[0:N]
        nums2 = nums[1:N+1]
        print(nums1)
        print(nums2)
        newN = len(nums1) - 1

        cars1 = [None for i in range(N+1)]
        cars2 = [None for i in range(N+1)]

        cars1[newN+1] = 0
        cars1[newN] = nums1[newN]

        cars2[newN+1] = 0
        cars2[newN] = nums2[newN]

        for i in range(newN - 1, -1, -1):
            cars1[i] = max(cars1[i+1], nums1[i] + cars1[i+2])
            cars2[i] = max(cars2[i+1], nums2[i] + cars2[i+2])

        return max(cars1[0], cars2[0])