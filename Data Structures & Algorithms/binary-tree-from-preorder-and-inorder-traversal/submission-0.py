# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        n = len(inorder)
        for i in range(n):
            inorder_index[inorder[i]] = i
        
        def constructTree(preorder: List[int], inorder: dict[int, int], current: int, left: int, right: int) -> TreeNode:
            if (left > right):
                return None
            mid = inorder[preorder[current]]
            node = TreeNode(preorder[current])
            left_span = mid - left+1
            node.left = constructTree(preorder, inorder, current+1, left, mid-1)
            node.right = constructTree(preorder, inorder, current + left_span, mid+1, right)

            return node

        return constructTree(preorder, inorder_index, 0, 0, n-1)