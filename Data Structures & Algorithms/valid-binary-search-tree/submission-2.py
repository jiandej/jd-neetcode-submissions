# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.prev = -float("inf")
        return self.inorderTraversal(root)
        
    
    def inorderTraversal(self, node: TreeNode) -> bool:
        if not node:
            return True
        
        is_valid = self.inorderTraversal(node.left)
        if not is_valid:
            return False
        if (self.prev >= node.val):
            return False
        self.prev = node.val
        return self.inorderTraversal(node.right)
        
