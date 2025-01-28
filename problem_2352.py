from collections import Counter
from typing import List


# 2352. Equal Row and Column Pairs

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
# Example 1:
# 3 2 1
# 1 7 6
# 2 7 7
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]

# Example 2:
# 3 1 2 2
# 1 4 4 5
# 2 4 2 2
# 2 4 2 2
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # # taken from solutions list
        # rows_counter = Counter(tuple(r) for r in grid)
        # transpose_matrix = zip(*grid)
        # columns_counter = Counter(tuple(r) for r in transpose_matrix)
        #
        # result = 0
        # for t in rows_counter:
        #     if t in columns_counter:
        #         result += rows_counter[t]*columns_counter[t]
        #
        # return result

        # my own
        result = 0

        row_map = {}
        # navigate though each row and put it in hash
        for row in grid:
            row_as_str = str(tuple(row))
            if row_as_str in row_map:
                row_map[row_as_str] += 1
            else:
                row_map[row_as_str] = 1

        transpose_matrix = zip(*grid)
        for col in transpose_matrix:
            col_as_str = str(col)
            if col_as_str in row_map:
                result += row_map[col_as_str]

        return result


# test
if __name__ == '__main__':
    print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1)
    print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3)
