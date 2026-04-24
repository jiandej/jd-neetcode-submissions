# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node: TreeNode, current_max: int):
            if not node:
                return
            
            if (node.val >= current_max):
                self.count+=1
            
            current_max = max(current_max, node.val)
            dfs(node.left, current_max)
            dfs(node.right, current_max)
        
        dfs(root, root.val)

        return self.count