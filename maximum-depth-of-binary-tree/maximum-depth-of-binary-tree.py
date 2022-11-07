# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max = 0
        return self.findMax(root,0)
        
    def findMax(self,tree, max):

        if tree:
            max = max+ 1
            left_max = self.findMax(tree.left, max)
            right_max = self.findMax(tree.right, max)
            
            if left_max > max:
                max = left_max
            if right_max > max:
                max = right_max
        
            return max
        else:
            return max

        