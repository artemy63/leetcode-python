# 328. Odd Even Linked List

from typing import Optional


# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr_odd_head = head  # текущий нечетный элемент
        even_head = head.next  # первый четный элемент, куда мы замкнём цепь
        curr_even_head = head.next  # текущий четный элемент

        while curr_even_head is not None and curr_even_head.next is not None:
            curr_odd_head.next = curr_even_head.next  # текущий нечетный теперь смотрит на следующий после четного
            curr_odd_head = curr_even_head.next  # текущий четный это теперь тот, на который мы ему поменяли ссылку
            curr_even_head.next = curr_even_head.next.next
            curr_even_head = curr_odd_head.next

        curr_odd_head.next = even_head

        return head


# test
if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().oddEvenList(head)
    curr_head = head
    while curr_head is not None:
        print('element ' + str(curr_head.val))
        curr_head = curr_head.next
