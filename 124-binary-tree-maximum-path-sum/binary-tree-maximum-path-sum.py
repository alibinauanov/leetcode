# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.pathSum = root.val

        def helper(root):
            if not root:
                return
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))

            currPath = root.val + left + right

            self.pathSum = max(self.pathSum, currPath)

            return root.val + max(left, right)
        
        helper(root)
        return self.pathSum