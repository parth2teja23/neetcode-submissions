# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)


            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        if arr[0] == "null":
            return None
        root = TreeNode(arr[0])
        q = deque()
        q.append(root)
        i = 1
        while q:
            node = q.popleft()
            if arr[i] != "null":
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1
            if arr[i] != "null":
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1

        return root


