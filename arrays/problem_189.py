from typing import List


# 189. Rotate Array
#
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # approach #1, use additional space
        if k > len(nums):
            k = k % len(nums)

        second_arr = []
        for idx in range(len(nums) - k, len(nums)):
            second_arr.append(nums[idx])

        for idx in range(0, len(nums) - k):
            second_arr.append(nums[idx])

        for idx in range(0, len(nums)):
            nums[idx] = second_arr[idx]

        # approach #2, not use additional space
        # for i in range(1, k + 1):
        #     last = nums[len(nums) - 1]
        #     for idx in range(len(nums) - 1, 0, -1):
        #         nums[idx] = nums[idx - 1]
        #     nums[0] = last

# test
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    print(nums == [5, 6, 7, 1, 2, 3, 4])

    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, 2)
    print(nums == [3, 99, -1, -100])

    nums = [1, 2]
    Solution().rotate(nums, 3)
    print(nums == [2, 1])
