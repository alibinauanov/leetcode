# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def helper(node, currSum):
            if not node:
                return 0
            
            currSum += node.val
            countPath = 1 if currSum == targetSum else 0

            countPath += helper(node.left, currSum)
            countPath += helper(node.right, currSum)

            return countPath
        
        def traverse(node):
            if not node:
                return 0
            
            currPath = helper(node, 0)
            leftPathSum = traverse(node.left)
            rightPathSum = traverse(node.right)

            return currPath + leftPathSum + rightPathSum
            
        return traverse(root)