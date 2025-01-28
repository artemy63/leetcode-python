from typing import List


# 735. Asteroid Collision

# We are given an array asteroids of integers representing asteroids in a row.
# The indices of the asteriod in the array represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
#
# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
#
# Constraints:
# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        for idx in range(len(asteroids) - 1, -1, -1):
            if asteroids[idx] * asteroids[idx - 1] < -1:  # they have different signs
                if abs(asteroids[idx] > abs(
                        asteroids[idx - 1])):  # if right is bigger than left, destroy right and move right to the left
                    asteroids[idx - 1] = asteroids[idx]
                    asteroids[idx] = 0
                elif abs(asteroids[idx]) < abs(asteroids[idx - 1]):  # right is smaller than left, destroy it
                    asteroids[idx] = 0
                else:  # destroy both
                    asteroids[idx] = 0
                    asteroids[idx - 1] = 0

        return [a for a in asteroids if a != 0]


# test
if __name__ == '__main__':
    print(Solution().asteroidCollision([5, 10, -5]) == [5, 10])
    print(Solution().asteroidCollision([8, -8]) == [])
    print(Solution().asteroidCollision([10, 2, -5]) == [10])
    # WTF ???
    print(Solution().asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2])
