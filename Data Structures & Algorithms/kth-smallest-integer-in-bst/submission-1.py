# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def inorderTraversal(node: Optional[TreeNode], k: int) -> Optional[int]:
            if not node:
                return None
            left_val = inorderTraversal(node.left, k)
            if left_val:
                return left_val
            self.count += 1
            if (k == self.count):
                # early stop here
                return node.val
            right_val = inorderTraversal(node.right, k)
            if right_val:
                return right_val
        
        result = inorderTraversal(root, k)

        return result
