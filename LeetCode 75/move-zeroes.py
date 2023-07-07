class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for s in range (nums.count(0)):
            for i, num in enumerate(nums):
                if num == 0:
                    nums.pop(i)
                    nums.append(0)
                    break

    def betterSolution(self, nums: List[int]) -> None:
        '''
        Fast pointer and slow pointer.
        '''
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1