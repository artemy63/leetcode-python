# 238. Product of Array Except Self

from typing import List


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # in order to don't affect multiplication
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        result = [0] * len(nums)

        # calculate products of all elements to left from given, first element is 1
        pref[0] = 1
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]

        # calculate products of all elements to right from given, first element is 1
        suff[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        # in prev[i] we have products of all elements to left, in suff[i] products of all elements to right for given
        # so it product will contain all elements of source array exclude the given
        for i in range(0, len(nums)):
            result[i] = pref[i] * suff[i]

        return result


# test
if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
    print(Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
