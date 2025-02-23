from typing import List


# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
#
# Example 3:
# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        element_dict = {}
        for num in nums:
            if num in element_dict:
                element_dict.pop(num)
            else:
                element_dict[num] = 1

        for k in element_dict.keys():
            return k


# test
if __name__ == '__main__':
    print(Solution().singleNumber([2, 2, 1]) == 1)
    print(Solution().singleNumber([4, 1, 2, 1, 2]) == 4)
    print(Solution().singleNumber([1]) == 1)
