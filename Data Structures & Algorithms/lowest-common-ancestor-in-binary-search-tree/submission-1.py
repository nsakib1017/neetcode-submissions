# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            if p.val > cur.val and q.val > cur.val:
                stack.append(cur.right)
            elif p.val < cur.val and q.val < cur.val:
                stack.append(cur.left)
            else:
                return cur