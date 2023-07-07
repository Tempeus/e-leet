def merge(nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1cpy = nums1[:m]
        n1idx = 0
        n2idx = 0

        for i in range(n+m):
            if n1idx >= m:
                 nums1[i] = nums2[n2idx]
                 n2idx += 1
            elif n2idx >= n:
                 nums1[i] = num1cpy[n1idx]
                 n1idx += 1
                 
            elif n1idx < m and n2idx < n and num1cpy[n1idx] >= nums2[n2idx]:
                nums1[i] = nums2[n2idx]
                n2idx += 1
            elif n2idx < n and n1idx < m and num1cpy[n1idx] < nums2[n2idx]:
                nums1[i] = num1cpy[n1idx]
                n1idx += 1
        print(nums1)

if __name__ == "_main_":
     merge([1,2,3,0,0,0] ,3, [2,5,6], 3)