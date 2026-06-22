# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftMax, rightMax = self.maxDepth(root.left), self.maxDepth(root.right)
        val = max(leftMax, rightMax) + 1

        return val