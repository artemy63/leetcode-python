from typing import Optional


# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
# the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:\
        # approach #1
        # already_passed = []
        #
        # curr = head
        # while curr and curr.next:
        #     if curr.next in already_passed:
        #         return True
        #     else:
        #         already_passed.append(curr.next)
        #
        #     curr = curr.next
        #
        # return False

        # approach #2
        # O(1) for memory, two pointers
        slow_p, fast_p = head, head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if fast_p == slow_p:
                return True

        return False