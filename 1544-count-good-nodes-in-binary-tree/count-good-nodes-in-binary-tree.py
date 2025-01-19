# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, maxVal):
            if not node:
                return 0
                
            counter = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            leftMax = helper(node.left, maxVal)
            rightMax = helper(node.right, maxVal)

            return counter + leftMax + rightMax
        
        return helper(root, root.val)