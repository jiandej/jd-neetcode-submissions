# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = collections.deque()

        queue.append(root)

        while queue:
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                if (self.isSameTree(node, subRoot)):
                    return True
                else:
                    if (node.left):
                        queue.append(node.left)
                    if (node.right):
                        queue.append(node.right)
        
        return False
    
    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if (not node1 and not node2):
            return True
        if (not node1 or not node2 or node1.val != node2.val):
            return False
        
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)