from typing import List


# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # result = []
        # for num in nums:
        #     result.append(num * num)
        #
        # result.sort()
        #
        # return result

        # approach two
        result = [0] * len(nums)
        left_pointer = 0
        right_pointer = len(nums) - 1

        for idx in range(len(nums) - 1, -1, -1):
            if abs(nums[right_pointer]) > abs(nums[left_pointer]):
                result[idx] = nums[right_pointer] * nums[right_pointer]
                right_pointer -= 1
            else:
                result[idx] = nums[left_pointer] * nums[left_pointer]
                left_pointer += 1

        return result


# test
if __name__ == '__main__':
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100])
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121])
