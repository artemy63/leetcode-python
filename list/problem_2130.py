# 2130. Maximum Twin Sum of a Linked List

from typing import Optional


# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
#
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.
#
# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6.

# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.

# Example 3:
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

# Constraints:
# The number of nodes in the list is an even integer in the range [2, 105].
# 1 <= Node.val <= 105

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # main idea
        # navigate through input LL until reach the end and do next staff
        # define the middle of the list, reverse links from first half of it
        # 1 <- 2 - 3 -> 4
        # it seems that I need three pointers:
        # one to point of the end of first half (2)
        # second to the end of list itself
        # third to the beginning of second half of list

        fh_pointer_prev = None
        fh_pointer = head

        sh_pointer = head.next # atr least 2 elements in the list
        curr_pointer = sh_pointer # to define end of list

        while curr_pointer.next and curr_pointer.next.next:
            # reverse first half
            fh_pointer.next = fh_pointer_prev
            fh_pointer_prev = fh_pointer
            fh_pointer = sh_pointer

            sh_pointer = sh_pointer.next
            curr_pointer = curr_pointer.next.next

            fh_pointer.next = fh_pointer_prev

        max_sum_of_twins = 0

        while fh_pointer and sh_pointer:
            max_sum_of_twins = max(max_sum_of_twins, fh_pointer.val + sh_pointer.val)
            fh_pointer = fh_pointer.next
            sh_pointer = sh_pointer.next

        return max_sum_of_twins

# test
if __name__ == '__main__':
    ll = ListNode(1, ListNode(100000, None))
    print(Solution().pairSum(ll) == 100001)

    ll = ListNode(5, ListNode(4, ListNode(2, ListNode(1, None))))
    print(Solution().pairSum(ll) == 6)

    ll = ListNode(4, ListNode(2, ListNode(2, ListNode(3, None))))
    print(Solution().pairSum(ll) == 7)
