# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = []
        curr = root
        lastvisited = None
        gain = {}
        res = root.val

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            peek = stack[-1]

            if peek.right and lastvisited != peek.right:
                curr = peek.right
            else:
                stack.pop()

                leftMax = max(gain.get(peek.left, 0), 0)
                rightMax = max(gain.get(peek.right, 0), 0)

                res = max(res, peek.val + leftMax + rightMax)

                gain[peek] = peek.val + max(leftMax, rightMax)
                lastvisited = peek
        return res
