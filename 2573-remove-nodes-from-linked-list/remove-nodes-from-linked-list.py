# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Recursively process the rest of the list
        head.next = self.removeNodes(head.next)
        
        # If the next node has a greater value, return the next node
        # Otherwise, keep the current node
        if head.next and head.next.val > head.val:
            return head.next
        else:
            return head