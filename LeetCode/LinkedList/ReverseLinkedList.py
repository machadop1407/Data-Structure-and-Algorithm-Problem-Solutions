# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        ptr = head
        while ptr:
            stack.append(ptr.val)
            ptr = ptr.next

        ptr2 = head
        while ptr2:
            ptr2.val = stack.pop()
            ptr2 = ptr2.next

        return head
