# 1448. Count Good Nodes in Binary Tree
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
# Example 1:
#         3
#        /  \
#       1     4
#      /      / \
#     3      1    5
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:
#         3
#        /
#       3
#      /  \
#     4     2
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:
#
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

# Constraints:
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node: TreeNode, curr_max: int) -> int:
            intermediate_answer = 0
            if node:
                if node.val >= curr_max:
                    intermediate_answer += 1

                return (intermediate_answer +
                        count_good_nodes(node.left, max(curr_max, node.val)) +
                        count_good_nodes(node.right, max(curr_max, node.val)))
            else:
                return intermediate_answer

        return count_good_nodes(root, root.val)


# test
if __name__ == '__main__':
    root_node = TreeNode(
        val=3,
        left=TreeNode(
            val=1,
            left=TreeNode(3)
        ),
        right=TreeNode(
            val=4,
            left=TreeNode(1),
            right=TreeNode(5)
        )
    )
    print(Solution().goodNodes(root_node) == 4)

    root_node = TreeNode(
        val=3,
        left=TreeNode(
            val=3,
            left=TreeNode(4),
            right=TreeNode(2)
        )
    )
    print(Solution().goodNodes(root_node) == 3)

    root_node = TreeNode(1)
    print(Solution().goodNodes(root_node) == 1)
