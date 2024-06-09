def find_number(nums):
    nums = set(nums)
    ans = []

    for i in range(len(nums)):
        if nums[i] + 1 not in nums and nums[i] - 1 not in nums:
            ans.append(nums[i])
    
    return ans
