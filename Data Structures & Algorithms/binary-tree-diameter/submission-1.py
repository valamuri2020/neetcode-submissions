# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0

            # localBest, longestPath
            leftBest, leftLongest = dfs(node.left)
            rightBest, rightLongest = dfs(node.right)

            nodeBest, nodeLongest = max(leftBest, rightBest, leftLongest + rightLongest), max(leftLongest, rightLongest) + 1
            return nodeBest, nodeLongest
        
        return dfs(root)[0]
        





