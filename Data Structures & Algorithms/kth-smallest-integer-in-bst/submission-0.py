# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.count = 0

        def inorderTraversal(node: Optional[TreeNode], k: int):
            if not node:
                return
            inorderTraversal(node.left, k)
            self.count += 1
            if (k == self.count):
                self.result = node.val
                # early stop here
                return
            inorderTraversal(node.right, k)
        
        inorderTraversal(root, k)

        return self.result
