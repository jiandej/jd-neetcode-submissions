# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float("inf")

        # return the max path sum that used by parent node
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # only choose either left or right or not choosing either of them 
            max_path_sum = max(left, right, 0) + node.val

            # treat this node as the mid point and using both left and right subtree paths
            self.max_sum = max(self.max_sum, left + right + node.val, max_path_sum)

            return max_path_sum
        
        dfs(root)

        return self.max_sum