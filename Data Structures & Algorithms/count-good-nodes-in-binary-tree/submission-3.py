# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxSoFar = float("-inf")
        stack = [(root, maxSoFar)]
        goodNode = 0

        while stack:
            cur, maxSoFar = stack.pop()
            if not cur:
                continue
            if cur.val >= maxSoFar:
                goodNode+=1
                maxSoFar = cur.val
            stack.append((cur.left, maxSoFar))
            stack.append((cur.right, maxSoFar))
        return goodNode
