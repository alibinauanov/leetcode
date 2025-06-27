# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def countHelper(root, counter):
            if not root:
                return 0
            
            if root:
                counter[0] += 1
            
            countHelper(root.left, counter)
            countHelper(root.right, counter)
        
        counter = [0]
        countHelper(root, counter)
        return counter[0]

        # another solution:
        # if not root:
        #     return 0
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right)