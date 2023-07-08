class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_i = len(nums)
        first = 0
        next_value = k
        if(max_i - k == 0):
            return sum(nums) / k
        elif(k == 1):
            return max(nums)
        else:
            max_avg = sum(nums[first:next_value]) / k
            cur_avg = max_avg
            while next_value < max_i:
                cur_avg = cur_avg - float(nums[first]) / k
                cur_avg = cur_avg + float(nums[next_value]) / k
                max_avg = max_avg if max_avg > cur_avg else cur_avg
                first += 1
                next_value += 1
            return max_avg