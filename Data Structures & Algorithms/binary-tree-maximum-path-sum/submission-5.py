# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # include/exclude root
        # bestPathSum = max(leftSum, rightSum, leftSum+rightSum+node.val, node.val)
        # fullPathSum = max(rightSum, leftSum) + node.val

        res = float("-inf")
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            leftSum = max(leftSum, 0)
            rightSum = max(rightSum, 0)

            res = max([
                res, rightSum+leftSum+node.val
            ])

            return max(leftSum, rightSum) + node.val
        
        dfs(root)
        return res





        