# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            return root.val == subRoot.val and isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
        
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)