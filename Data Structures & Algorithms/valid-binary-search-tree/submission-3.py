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
        
        self.prev = None
        return self.inorderTraversal(root)
        
    
    def inorderTraversal(self, node: TreeNode) -> bool:
        if not node:
            return True
        
        if not self.inorderTraversal(node.left):
            return False
        if (self.prev is not None and self.prev >= node.val):
            return False
        self.prev = node.val
        return self.inorderTraversal(node.right)
        
