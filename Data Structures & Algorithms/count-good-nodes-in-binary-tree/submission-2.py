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
        countNodes = 0

        while stack:
            node, maxSoFar = stack.pop()
            if node:
                if node.val >= maxSoFar:
                    countNodes+=1
                    maxSoFar = max(maxSoFar, node.val)
                stack.append((node.left, maxSoFar))
                stack.append((node.right, maxSoFar))
        return countNodes