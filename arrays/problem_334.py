import sys
from typing import List


# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.
#
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # keep first and second element of triplet
        first_num, second_num = sys.maxsize, sys.maxsize

        # while iterating over whole input array we need to next thing:
        # compare current with first_num, if it less than first_num it will not affect existence of triplet
        # the same for second_num
        # if current more that both we've found a triplet
        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True

        return False


# test
if __name__ == '__main__':
    print(Solution().increasingTriplet([1, 2, 3, 4, 5]) == True)
    print(Solution().increasingTriplet([5, 4, 3, 2, 1]) == False)
    print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]) == True)
