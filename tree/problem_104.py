from collections import deque
from typing import Optional


# 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # corner case
        if not root:
            return 0

        # DFS
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS
        max_depth = 0
        nodes = deque()
        nodes.append(root)
        while nodes:
            max_depth += 1

            for _ in range(0, len(nodes)):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)

                if node.right:
                    nodes.append(node.right)

        return max_depth

# test
if __name__ == '__main__':
    node = TreeNode(
        val=3,
        left=TreeNode(9),
        right=TreeNode(
            20,
            left=TreeNode(15),
            right=TreeNode(7)
        )
    )

    print(Solution().maxDepth(node) == 3)
