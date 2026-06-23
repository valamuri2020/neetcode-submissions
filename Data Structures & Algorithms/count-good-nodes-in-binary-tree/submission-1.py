# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # propogate max val along branch down the chain so each node can eval if it's good
        # return isGood + goodNodes(node.left) + goodNodes(node.right)

        def dfs(node, maxSeenSoFar):
            if not node:
                return 0
            
            isGood = int(node.val >= maxSeenSoFar)
            leftGoodNodes = dfs(node.left, max(maxSeenSoFar, node.val))
            rightGoodNodes = dfs(node.right, max(maxSeenSoFar, node.val))

            return isGood + leftGoodNodes + rightGoodNodes
        
        return dfs(root, float('-inf'))