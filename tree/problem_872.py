from typing import Optional


# 872. Leaf-Similar Trees
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
#
#           3
#       /       \
#      5          1
#    /   \       / \
#   6      2    9    8
#         /  \
#        7    4
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Example 1:
#           3
#       /       \
#      5          1
#    /   \       / \
#   6      2    9    8
#         /  \
#        7    4
#
#           3
#       /       \
#      5          1
#    /   \       / \
#   6      7    4    2
#                   /  \
#                  9    8
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
# Example 2:
#       1                     1
#      /  \      and         /  \
#     2    3                3    2
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
# Constraints:
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node: TreeNode, leaves:[]):
            if node:
                if not node.left and not node.right:
                    leaves.append(node.val)
                else:
                    get_leaves(node.left, leaves)
                    get_leaves(node.right, leaves)

        first_tree_leaves = []
        second_tree_leaves = []
        get_leaves(root1, first_tree_leaves)
        get_leaves(root2, second_tree_leaves)

        return first_tree_leaves == second_tree_leaves

        # def dfs(node):
        #     if node:
        #         if not node.left and not node.right:
        #             yield node.val
        #         yield from dfs(node.left)
        #         yield from dfs(node.right)
        #
        # return list(dfs(root1)) == list(dfs(root2))


# test
if __name__ == '__main__':
    root_node_1 = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
    root_node_2 = TreeNode(val=1, left=TreeNode(3), right=TreeNode(2))
    print(Solution().leafSimilar(root_node_1, root_node_2) == False)

    root_node_1 = TreeNode(
        val=3,
        left=TreeNode(
            val=5,
            left=TreeNode(val=6),
            right=TreeNode(
                val=2,
                left=TreeNode(7),
                right=TreeNode(4)
            )
        ),
        right=TreeNode(
            val=1,
            left=TreeNode(9),
            right=TreeNode(8)
        )
    )
    root_node_2 = TreeNode(
        val=3,
        left=TreeNode(
            val=5,
            left=TreeNode(val=6),
            right=TreeNode(val=7)
        ),
        right=TreeNode(
            val=1,
            left=TreeNode(4),
            right=TreeNode(
                val=2,
                left=TreeNode(9),
                right=TreeNode(8)
            )
        )
    )
    print(Solution().leafSimilar(root_node_1, root_node_2) == True)
