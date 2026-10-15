# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gain = {}
        stack = [(root, False)]
        best = float("-inf")
        while stack:
            cur, expanded = stack.pop()
            if not cur:
                continue
            if expanded:
                left, right = max(gain.get(cur.left, 0), 0), max(gain.get(cur.right, 0), 0)
                best = max(best, cur.val+left+right)
                gain[cur] = cur.val + max(left, right)
            else:
                stack.append((cur, True))
                stack.append((cur.left, False))
                stack.append((cur.right, False))
        return best