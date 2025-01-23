# 2215. Find the Difference of Two Arrays
from typing import List


# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
#
# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

# Example 2:
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # # too slow
        # ans_left = []
        # ans_right = []
        #
        # for num in nums1:
        #     if num not in nums2 and num not in ans_left:
        #         ans_left.append(num)
        #
        # for num in nums2:
        #     if num not in nums1 and num not in ans_right:
        #         ans_right.append(num)
        #
        # return [ans_left, ans_right]

        ans_left = set()
        ans_right = set()
        first_elements_only = set()
        for num in nums1:
            first_elements_only.add(num)

        second_elements_only = set()
        for num in nums2:
            second_elements_only.add(num)
            if num not in first_elements_only:
                ans_right.add(num)

        for num in nums1:
            if num not in second_elements_only:
                ans_left.add(num)

        return [list(ans_left), list(ans_right)]


# test
if __name__ == '__main__':
    print(Solution().findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]])
    print(Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3],[]])
