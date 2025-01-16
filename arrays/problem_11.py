from typing import List


# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # # initial solution, just go from all possible variants and compare with current max, O(n^2), Limit exceeded ((
        # _result = 0
        # for i in range(0, len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         _min_height = min(height[i], height[j])
        #         _curr_result = _min_height * (j - i)
        #         if _curr_result > _result:
        #             _result = _curr_result
        #
        # return _result

        # pointers to beginning and end of the array
        _left_pointer = 0
        _right_pointer = len(height) - 1
        _max_area = 0
        # the idea of solution
        # on each step we calculate current area as taking min of current height and distance between elements in the array(width)
        # after that we move left or right border, depends on height, we throw away border with the min height, keeping there
        # height with higher height (sounds good, isn't it?)
        while _left_pointer < _right_pointer:
            _curr_area = min(height[_left_pointer], height[_right_pointer]) * (_right_pointer - _left_pointer)
            if _curr_area > _max_area:
                _max_area = _curr_area

            if height[_left_pointer] > height[_right_pointer]:
                _right_pointer -= 1
            elif height[_left_pointer] == height[_right_pointer]:
                if height[_left_pointer + 1] > height[_right_pointer - 1]:
                    _right_pointer -= 1
                else:
                    _left_pointer += 1
            else:
                _left_pointer += 1

        return _max_area

# test
if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49)
    print(Solution().maxArea([1,1]) == 1)
