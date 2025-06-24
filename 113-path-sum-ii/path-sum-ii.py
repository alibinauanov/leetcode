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
        :rtype: List[List[int]]
        """
        def helper(node, tempSum, path, res):
            if not node:
                return
            
            tempSum += node.val
            path.append(node.val)

            if not node.left and not node.right and tempSum == targetSum:
                res.append(list(path))
            
            helper(node.left, tempSum, path, res)
            helper(node.right, tempSum, path, res)

            path.pop()
        
        res = []
        helper(root, 0, [], res)
        return res