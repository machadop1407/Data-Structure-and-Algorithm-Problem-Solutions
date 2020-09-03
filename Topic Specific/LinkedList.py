
# Singly Linked List:


# Trasversing A LL:

def trasverse(self, head: ListNode) -> ListNode:
    while head:
        head = head.next
        print(head.val)

# Remove Duplicate From Sorted List


def deleteDuplicates(self, head: ListNode) -> ListNode:
    curr = head
    while curr is not None and curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
