# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.serialized_string = []

        def dfs(node: TreeNode):
            if not node:
                self.serialized_string.append("N")
            else:
                self.serialized_string.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            
        
        dfs(root)

        return ",".join(self.serialized_string)
            
            
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.current_idx = 0
        data_array = data.split(",")

        def dfs(data: list[str]) -> Optional[TreeNode]:
            if data[self.current_idx] == "N":
                self.current_idx += 1
                return None
            
            node_val = int(data[self.current_idx])
            self.current_idx += 1
            node = TreeNode(node_val)

            node.left = dfs(data)
            node.right = dfs(data)

            return node
        
        return dfs(data_array)


