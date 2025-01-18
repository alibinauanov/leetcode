# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def is_leaf(node):
            return node.left is None and node.right is None
        
        def helper(node):
            if not node:
                return 0
            if is_leaf(node):
                return 1
            else:
                leftDepth = helper(node.left)
                rightDepth = helper(node.right)
                return max(leftDepth, rightDepth) + 1
        
        if not root:
            return 0
        else:
            return helper(root)