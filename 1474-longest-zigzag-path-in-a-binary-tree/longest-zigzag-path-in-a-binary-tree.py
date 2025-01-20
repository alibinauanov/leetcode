# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(node, direction, length):
            if not node:
                return
            
            self.maxLength = max(self.maxLength, length)

            if direction == "left":
                helper(node.left, "right", length + 1)
                helper(node.right, "left", 1)
            elif direction == "right":
                helper(node.right, "left", length + 1)
                helper(node.left, "right", 1)
        
        self.maxLength = 0
        helper(root.left, "right", 1)
        helper(root.right, "left", 1)
        return self.maxLength