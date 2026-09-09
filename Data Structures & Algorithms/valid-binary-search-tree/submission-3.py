# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        dfsQ = deque([(root, float("-inf"), float("inf"))])

        while dfsQ:
            node, left, right = dfsQ.popleft()
            
            if not (left < node.val <right):
                return False
            if node.left:
                dfsQ.append((node.left, left, node.val))
            if node.right:
                dfsQ.append((node.right, node.val, right))
        return True

