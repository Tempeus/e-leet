from typing import List


def intersection(nums: List[List[int]]) -> List[int]:
        counts = {}
        len_nums = len(nums)
        answer = []

        for num in nums:
            for n in num:
                if n not in counts:
                    counts[n] = 1
                elif n in counts:
                    counts[n] += 1
        
        for number in counts:
            if counts.get(number) >= len_nums:
                answer.append(number)
        answer.sort()

        return answer

print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))