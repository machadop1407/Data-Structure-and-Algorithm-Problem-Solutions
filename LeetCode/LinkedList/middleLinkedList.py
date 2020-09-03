# Given a non-empty, singly linked list with head node head,
# return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# MY FIRST SUBMITION: Horrible Solution

import math


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        length = 0
        ptr = head

        while True:
            length += 1
            if ptr.next is None:
                break

            ptr = ptr.next

        if length % 2 == 0:
            middleIndex = int(length / 2)
        else:
            middleIndex = math.floor(length / 2)

        node = 0
        ptr2 = head
        while node < middleIndex:
            node += 1
            ptr2 = ptr2.next

        return ptr2


# Best Solution:

    # Create 2 pointers: slow and fast
    # Fast will move 2 as fast as slow, meaning that when fast reaches the end, slow must be half of fast (aka. the middle)

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
