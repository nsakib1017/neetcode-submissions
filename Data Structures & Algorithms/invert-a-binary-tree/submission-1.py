# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodeq = [root]

        while nodeq:
            node = nodeq.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                nodeq.append(node.left)
            if node.right:
                nodeq.append(node.right)
        return root

