# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # isSameTree = p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        # None == None

        def dfs(p_node, q_node):
            if not p_node and not q_node:
                return True
            
            return p_node is not None and q_node is not None and p_node.val == q_node.val and dfs(p_node.left, q_node.left) and dfs(p_node.right, q_node.right)
        
        return dfs(p, q)

