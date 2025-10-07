# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        p1, p2 = l1, l2

        while p1 is not None or p2 is not None or carry != 0:
            val1 = p1.val if p1 is not None else 0
            val2 = p2.val if p2 is not None else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
        return dummy.next