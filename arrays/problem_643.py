# 643. Maximum Average Subarray I

import sys
from typing import List


# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.
#
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_sum_of_sliding_window = -1 * sys.maxsize
        curr_sum_of_sliding_window = 0
        for i in range(0, k):
            curr_sum_of_sliding_window += nums[i]

        if curr_sum_of_sliding_window > max_sum_of_sliding_window:
            max_sum_of_sliding_window = curr_sum_of_sliding_window

        for i in range(k, len(nums)):
            curr_sum_of_sliding_window -= nums[i - k]
            curr_sum_of_sliding_window += nums[i]

            if curr_sum_of_sliding_window > max_sum_of_sliding_window:
                max_sum_of_sliding_window = curr_sum_of_sliding_window

        return float(max_sum_of_sliding_window / k)


#  test
if __name__ == '__main__':
    print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(Solution().findMaxAverage([5], 1))
