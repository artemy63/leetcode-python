from typing import List


# 1493. Longest Subarray of 1's After Deleting One Element

# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.
#
# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest_seq = 0
        left_idx = 0
        zero_count = 0

        for right_idx in range(0, len(nums)):
            if nums[right_idx] == 0:
                zero_count += 1

            # if there is more than one zero we need to move left border to right until we decrease number of zeroes in sequence
            while zero_count > 1:
                if nums[left_idx] == 0:
                    zero_count -= 1
                left_idx += 1

            longest_seq = max(longest_seq, right_idx - left_idx + 1)

        # because we need to delete one element, we counted longest_seq with extra 0
        return longest_seq - 1


# test
if __name__ == '__main__':
    print(Solution().longestSubarray([1, 1, 0, 1]) == 3)
    print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5)
    print(Solution().longestSubarray([1, 1, 1]) == 2)
