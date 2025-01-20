from typing import List


# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.
#
# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0

        # # first approach, brute force
        # # for each nums[i] handle numbers from nums[i+1]..nums[n] and check if they sum are k
        # # if so place into found plots -1
        # for i in range(0, len(nums) - 1):
        #     #
        #     if nums[i] == -1:
        #         continue
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == -1:
        #             continue
        #
        #         if nums[i] + nums[j] == k:
        #             result +=1
        #             nums[i] = -1
        #             nums[j] = -1
        #             break


        # # second approach
        # # sort input array, and use two pointers
        # nums.sort()
        # left_idx = 0
        # right_idx = len(nums) - 1
        # while left_idx < right_idx:
        #     if nums[left_idx] + nums[right_idx] == k:
        #         result += 1
        #         left_idx += 1
        #         right_idx -= 1
        #     elif nums[left_idx] + nums[right_idx] < k:
        #         left_idx += 1
        #     else:
        #         right_idx -= 1


        # third approach
        # use map to keep diff between desired sum (k) nd current element
        # if for current nums[i] we have an element with such key in map => we have a match
        paired_map = dict()
        for i in range(0, len(nums)):
            # diff between desired sum and current element
            paired = k - nums[i]
            # if pair for current already considered - we need to increase number of inclusions
            if paired in paired_map:
                result += 1
                paired_cnt = paired_map[paired]
                if paired_cnt == 1:
                    paired_map.pop(paired)
                else:
                    paired_map[paired] = (paired_map[paired] - 1)
            else:
                if nums[i] in paired_map.keys():
                    paired_map[nums[i]] = (paired_map[nums[i]] + 1)
                else:
                    paired_map[nums[i]] = 1

        return result


# test
if __name__ == '__main__':
    print(Solution().maxOperations([1, 2, 3, 4], 5) == 2)
    print(Solution().maxOperations([3, 1, 3, 4, 3], 6) == 1)
