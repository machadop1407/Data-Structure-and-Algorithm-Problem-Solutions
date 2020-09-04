# You are given two non-empty linked lists
# representing two non-negative integers. The
# digits are stored in reverse order and each
# of their nodes contain a single digit. Add
# the two numbers and return it as a linked
# list.

# You may assume the two numbers do not contain
# any leading zero, except the number 0 itself.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ptr1 = l1
        ptr2 = l2

        arr1 = []
        arr2 = []
        while ptr1:
            arr1.append(ptr1.val)
            ptr1 = ptr1.next

        while ptr2:
            arr2.append(ptr2.val)
            ptr2 = ptr2.next

        number1 = 0
        for i in reversed(arr1):
            number1 = (number1 * 10) + i

        number2 = 0
        for i in reversed(arr2):
            number2 = (number2 * 10) + i

        result = str(number1 + number2)

        finalLL = ListNode(None)
        for i in reversed(result):
            newNode = ListNode(i)
            ptr = finalLL
            while (ptr.next != None):
                ptr = ptr.next
            ptr.next = newNode

        return finalLL.next
