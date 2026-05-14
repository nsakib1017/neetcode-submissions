# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        stack = []
        lastVisited = None
        depths = {}
        curr = root
        
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

                if abs(left-right) > 1:
                    return False
                depths[peek] = 1 + max(left, right)
                lastVisited = peek
        return True
