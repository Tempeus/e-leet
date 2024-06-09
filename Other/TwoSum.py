from typing import List


def TwoSum(nums, target) -> List[int]:
    hashmap = {}

    for i in range(len(nums)):
        pair = target - nums[i]
        if pair in hashmap.keys():
            return [hashmap.get(pair), i]
        else:
            hashmap[nums[i]] = i


if __name__ == "__main__":
    '''
    If 5 is the answer, it must be paired with:
    target - 5 = 3

    store values in hashmap - {Number: index}
    '''
    nums = [3,2,4]
    target = 6
    print(TwoSum(nums, target))
