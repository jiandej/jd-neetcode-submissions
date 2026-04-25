# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val:idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0
        
        def constructTree(preorder: List[int], inorder: dict[int, int], left: int, right: int) -> TreeNode:
            if (left > right):
                return None
            node_val = preorder[self.preorder_idx]
            mid = inorder[node_val]
            node = TreeNode(node_val)
            self.preorder_idx += 1

            node.left = constructTree(preorder, inorder, left, mid-1)
            node.right = constructTree(preorder, inorder, mid+1, right)

            return node

        return constructTree(preorder, inorder_index, 0, len(inorder)-1)