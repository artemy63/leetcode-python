from typing import List


# There is a biker going on a road trip.
# The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.
#
# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example 2:
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt = 0
        curr_alt = 0
        for altitude in gain:
            curr_alt += altitude
            if highest_alt < curr_alt:
                highest_alt = curr_alt

        return highest_alt


if __name__ == '__main__':
    print(Solution().largestAltitude([-5, 1, 5, 0, -7]) == 1)
    print(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0)
