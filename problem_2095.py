from typing import Optional


# 2095. Delete the Middle Node of a Linked List

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.

# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.

# Example 3:
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
#
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 1 <= Node.val <= 105

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = head
        # slow_pointer = head
        # fast_pointer = head
        # number_of_nods = 0
        #
        # if head.next is None:
        #     return None
        #
        # while fast_pointer.next is not None:
        #     number_of_nods += 1
        #     fast_pointer = fast_pointer.next
        #
        #     if number_of_nods % 2 == 1:
        #         prev = slow_pointer
        #         slow_pointer = slow_pointer.next
        #
        # if slow_pointer.next is None:
        #     prev.next = None
        # else:
        #     prev.next = slow_pointer.next
        #
        # return head


        if not head or not head.next:
            return None

        # slow pointer, by one element each time, point to head at first time
        slow = last_slow = head
        # fast pointer, set to second element of linked list
        fast = head.next            # 2
        while fast and fast.next:
            last_slow = slow
            slow = slow.next        # 2
            fast = fast.next.next   # 4
        # Even number of elements; use `slow`
        # eg. n = 4; 2 -> x -> 4
        if fast and not fast.next:
            slow.next = slow.next.next
        # Odd number of elements; use `last_slow`
        # eg. n = 5; 2 -> x -> 4
        else:  # fast is None
            last_slow.next = last_slow.next.next
        return head


# test
if __name__ == '__main__':
    preparedListNode = ListNode(1)
    # preparedListNode = ListNode(2, ListNode(1))
    # preparedListNode = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    Solution().deleteMiddle(preparedListNode)
