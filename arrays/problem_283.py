# 283. Move Zeroes

from typing import List


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n^2)
        # p_to_non_zero = None
        # for i in range(0, len(nums)):
        #     # find first zero
        #     if not nums[i]:
        #         #  todo check borders
        #         for j in range(i + 1, len(nums)):
        #             if nums[j]:
        #                 p_to_non_zero = j
        #                 break
        #
        #         if p_to_non_zero:
        #             nums[i], nums[p_to_non_zero] = nums[p_to_non_zero], nums[i]
        #             p_to_non_zero = None
        #
        #
        # print(nums)

        # idea is to move all not-null elements to beginning of the array
        # if we found the not-null element we swap it with element at index last_non_zero_found_at
        last_non_zero_found_at = 0
        for cur in range(0, len(nums)):
            if nums[cur]:
                nums[cur], nums[last_non_zero_found_at] = nums[last_non_zero_found_at], nums[cur]
                last_non_zero_found_at += 1

        print(nums)


#  test
if __name__ == '__main__':
    src_array = [0, 1, 0, 3, 12]
    Solution().moveZeroes(src_array)
    print(src_array == [1, 3, 12, 0, 0])

    src_array = [0]
    Solution().moveZeroes(src_array)
    print(src_array == [0])

    src_array = [4, 0, 1, 0, 3, 12]
    Solution().moveZeroes(src_array)
    print(src_array == [4, 1, 3, 12, 0, 0])
