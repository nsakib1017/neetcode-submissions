# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q=deque([(root, float("-inf"), float("inf"))])
        while q:
            cur, leftVal, rightVal = q.popleft()
            if not cur:
                continue
            if not leftVal < cur.val < rightVal:
                return False
            q.append((cur.left, leftVal, cur.val))
            q.append((cur.right, cur.val, rightVal))
        return True