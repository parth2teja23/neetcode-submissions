# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        MAX = root.val
        self.count = 0
        def dfs(root, MAX):
            if not root:
                return
            if root.val >= MAX:
                self.count += 1
            MAX = max(root.val, MAX)
            dfs(root.left, MAX)
            dfs(root.right, MAX)
        dfs(root, MAX)
        return self.count

