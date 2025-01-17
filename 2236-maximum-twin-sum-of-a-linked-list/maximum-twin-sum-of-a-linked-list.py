# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # 1)find the middle
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2)reverse the second half of list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # 3)set: first = head, second = head
        maxSum = 0
        first = head
        second = prev
        # 4)max(first.val + first.next.next.val, second.val + second.next.next.val)
        while second:
            maxSum = max(maxSum, first.val + second.val)
            first = first.next
            second = second.next
        return maxSum