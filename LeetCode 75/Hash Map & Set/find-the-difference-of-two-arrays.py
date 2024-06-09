class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = []
        answer2 = []

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        for num in nums1_set:
            match = False
            for i in nums2:
                if num == i:
                    match = True
                    break
            if not match:
                answer1.append(num)

        for num in nums2_set:
            match = False
            for i in nums1:
                if num == i:
                    match = True
                    break
            if not match:
                answer2.append(num)

        return [answer1, answer2]    
            