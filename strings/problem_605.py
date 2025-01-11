from typing import List


# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible_plants = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = i == 0 or flowerbed[i - 1] == 0
                empty_right_plot = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_plot:
                    # Remember that we plant in that plot
                    flowerbed[i] = 1
                    possible_plants += 1

        return possible_plants >= n


# test
if __name__ == '__main__':
    print(Solution().canPlaceFlowers(flowerbed=[1,0,0,0,1], n=1) == True)
    print(Solution().canPlaceFlowers(flowerbed=[1,0,0,0,1], n=2) == False)
    print(Solution().canPlaceFlowers(flowerbed=[1,0,0,0,0,1], n=2) == False)
    print(Solution().canPlaceFlowers(flowerbed=[1,0,0], n=1) == True)
    print(Solution().canPlaceFlowers(flowerbed=[1,0,0,1], n=1) == False)
    print(Solution().canPlaceFlowers(flowerbed=[0], n=1) == True)
    print(Solution().canPlaceFlowers(flowerbed=[0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0], n=17) == False)
