# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = []
        depths = {}
        lastVisited = None
        curr = root
        diameter = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            peek = stack[-1]

            if peek.right and lastVisited != peek.right:
                curr = peek.right
            else:
                stack.pop()
                left = depths.get(peek.left, 0)
                right = depths.get(peek.right, 0)

                diameter = max(diameter, left+right)

                depths[peek] = 1 + max(left, right)

                lastVisited = peek
        
        return diameter
                

