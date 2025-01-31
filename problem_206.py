from typing import Optional


# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initial state 1 -> 2 -> 3 -> 4 -> 5 -> None
        # desired state 5 -> 4 -> 3 -> 2 -> 1 -> None
        prev = None
        curr = head # first ListNode element

        while curr is not None:
            # get right element from the current, 2
            next_node = curr.next

            # reverse link for current node to previous, 1
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

