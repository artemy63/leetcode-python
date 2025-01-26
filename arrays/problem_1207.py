from typing import List


# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # intuitive idea
        # go through input array and store in map number of occurrence for each element
        # compare len of set of all values and len of all values

        occurrencies = dict()
        for el in arr:
            if el in occurrencies:
                occurrencies[el] = occurrencies[el] + 1
            else:
                occurrencies[el] = 1

        return len(occurrencies.values()) == len(set(occurrencies.values()))


# test
if __name__ == '__main__':
    print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]) == True)
    print(Solution().uniqueOccurrences([1, 2]) == False)
    print(Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True)
