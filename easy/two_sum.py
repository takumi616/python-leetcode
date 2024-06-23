#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        result = []
        for index, value in enumerate(nums):
            idx = dict.get(value)
            if idx != None:
                result.append(idx)
                result.append(index)
                break

            dict[target - value] = index

        return result


nums = [2,7,11,9,10]
target = 16
print(Solution().twoSum(nums, target))