# 1004. Max Consecutive Ones III
from typing import List


# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#
# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        longest_seq, left_idx, zero_cnt = 0, 0, 0

        # move right border until we use all possible flips of zeroes
        for right_idx in range(0, len(nums)):
            if nums[right_idx] == 0:
                zero_cnt += 1

            # move left border until we will be able to use possible zeroes
            while zero_cnt > k:
                if nums[left_idx] == 0:
                    zero_cnt -= 1
                left_idx += 1

            longest_seq = max(longest_seq, right_idx - left_idx + 1)

        return longest_seq


# test
if __name__ == '__main__':
    print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6)
    print(Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10)
